import os, string, re, random, time
import MetaforNL
from types import *

class Metafor:

    objects = [] 

    def __init__(self):
        print('Loading Metafor...')
        self.nl = MetaforNL.MetaforNL(self)

        # make the global function object called __main__
        sys_args = [] # none
        main_object = self.new_function_object('__main__',sys_args)
        self.objects = [main_object]

        # set focus on main
        self.focus = '__main__'
        self.top_level_focus = '__main__'

        # define a focus stack, in case we move in and out of focii
        self.focus_stack = ['__main__']

    def get_context(self):
        # returns one of two contexts: descriptive and procedural
        # e.g. descriptive if in __main__ or inside a class
        # e.g. procedural if inside a function

        if self.focus == '__main__' or self.type(self.focus) == 'ClassType':
            return 'descriptive'
        else:
            return 'procedural'

    def fullname_exists_p(self,full_name):
        res = self.get_object_ptr(full_name)
        if res != None:
            return 1
        else:
            return 0
            
    def resolve_name(self,local_name):
        # looks up the local_name
        # first in the current scope focus
        # if not found, keeps zooming out focus
        # until it is found
        # also, try pluralizing the local_name and searching

        # if does not exist, returns ''
        if local_name.strip() == '':
            return ''

        # first check if local_name is in the current_dir
        # need this case to handle name hidden in function args
        local_dir = map(lambda x:self.relativize_name(x,self.focus),self.dir())
        if local_name in local_dir:
            return self.focus+'.'+local_name
        
        # handle case of game 's score
        if local_name.find('_s_')!=-1:
            local_name='.'.join(local_name.split('_s_'))
        print "DEB1",local_name
        current_scope = self.focus
        while current_scope.strip() != '':
            segments = local_name.split('.')
            local_name_variants = ['the_'+segments[0],segments[0],]
            for segment in segments[1:]:
                roots = tuple(local_name_variants)
                local_name_variants = map(lambda x: x+'.the_'+segment,roots)+map(lambda x: x+'.'+segment,roots)
            print "DEB",local_name_variants,'SCOPE',current_scope
            reses = filter(lambda x:x!=None,map(lambda x:self.get_object_ptr(current_scope+'.'+x),[local_name]+local_name_variants))
            if len(reses)>0:
                return reses[0][0]
            else:
                current_scope = self.parent(current_scope)
                continue
        return ''
        
    def handle_query(self,query):
        response = self.nl.process(query)
        return response
        
    def pp_state_information(self):
        output = 'FOCUS: '+self.focus + '\n\n'
        output = 'FOCUS STACK: '+str(self.focus_stack) + '\n\n'
        output = 'DEICTIC STACK: '+str(self.nl.deictic_stack) +'\n\n'
        output += 'DIR: '+str(self.dir()) + '\n\n'
        output += 'CODETREE: '+str(self.objects)
        return output

    def type(self,full_name):
        obj_ptr = self.get_object_ptr(full_name)
        if obj_ptr:
            return obj_ptr[1]
        else:
            return None

    def relativize_name(self,name_to_relativize,relative_to_this_name):
        ntr = name_to_relativize.split('.')
        rttn = relative_to_this_name.split('.')
        relative_name = ntr
        for i in range(len(ntr)):
            if i in range(len(rttn)) and ntr[i]==rttn[i]:
                continue
            else:
                relative_name = ntr[i:]
                break
        return string.join(relative_name,'.')
                
    def local_name(self,full_name):
        # strips the inheritance dotted notation from full_name
        return full_name.split('.')[-1]

    def render_code(self,full_name='__main__',flavor='python'):
        # renders the code using different language engines
        # defaults to python
        if flavor=='clisp':
            return self.render_code_cl(full_name)
        elif flavor=='howTo':
            return self.render_code_howTo(full_name) 
        else:
            return self.render_code_python(full_name)
        
    def render_code_howTo(self, full_name='__main__'):
        cur_flavor = 'howTo'
        indent = '     '
        # recursively generates the code below a given object
        cur_object = self.get_object_ptr(full_name)
        #print "DEBUG2",full_name,cur_object
        cur_object_full_name,cur_object_type,cur_object_header,cur_object_body = cur_object
        if cur_object_type == 'ExecutionType':
            # e.g. "pacman.eat(dot)" ==> [SOMEGENERATEDNAME,'ExecutionType',['pacman.eat','FunctionType',[arguments list]],[]]
            output = self.relativize_name(cur_object_header[0],cur_object_full_name)
            if cur_object_header[1]=='FunctionType':
                args = string.join(cur_object_header[2],', ')
                function_ending = '('+args+')'
                output += function_ending
        elif cur_object_type == 'DefinitionType':
            short_var_name = self.local_name(cur_object_full_name)
            value = cur_object_header[0]
            #print "DEBUG4:",value
            output = short_var_name + ' = ' + value
#        elif cur_object_type == 'CondType':
#            if cur_object_header.strip(' ()')=='':
#                output = 'else: '+'\n'
#            else:
#                output = 'if '+cur_object_header+':' + '\n'
#            body_output = ''
#            for child_full_name in self.children(full_name):
#                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
#            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
#            output += body_output
#        elif cur_object_type == 'LoopType':
#            output = 'for '+cur_object_header[0]+' in '+cur_object_header[1]+':' + '\n'
#            body_output = ''
#            for child_full_name in self.children(full_name):
#                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
#            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
#            output += body_output
        elif cur_object_type == 'FunctionType':
            output = 'call '+self.local_name(cur_object_full_name)+'('+string.join(cur_object_header,', ')+') {' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                #print "DEBUG child_full_name",child_full_name,"self.children(full_name):",self.children(full_name),"full_name",full_name
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            if not body_output:
                body_output = '\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output + '\n}'
        elif cur_object_type == 'ClassType':
            if len(cur_object_header) > 0:
                inheritance_string = '('+string.join(cur_object_header,', ')+')'
            else:
                inheritance_string = ''
            output = 'module '+self.local_name(cur_object_full_name)+inheritance_string+':' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            if not  body_output:
                body_output += '\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'ListType':
            output = self.local_name(cur_object_full_name) + ' = ['+string.join(cur_object_header,', ')+']'
        else:
            output = 'ERROR: Unknown type can\'t be rendered!'
        return output

    def render_code_cl(self,full_name='__main__'):
        cur_flavor = 'clisp'
        indent = '     '
        # recursively generates the code below a given object
        cur_object = self.get_object_ptr(full_name)
        #print "DEBUG2",full_name,cur_object
        cur_object_full_name,cur_object_type,cur_object_header,cur_object_body = cur_object
        if cur_object_type == 'ExecutionType':
            # e.g. "pacman.eat(dot)" ==> [SOMEGENERATEDNAME,'ExecutionType',['pacman.eat','FunctionType',[arguments list]],[]]
            if cur_object_header[1]=='FunctionType':
                args = ' '+' '.join(cur_object_header[2])
            else:
                args = ''
            if self.parent(cur_object_header[0]) == self.local_name(cur_object_full_name):
                cur_self = 'self'
            else:
                cur_self = self.parent(cur_object_header[0])

            member_name = self.local_name(cur_object_header[0])
            output = "(%s %s%s)"%(member_name,cur_self,args)

        elif cur_object_type == 'DefinitionType':
            short_var_name = self.local_name(cur_object_full_name)
            value = cur_object_header[0]
            # fix: rewrite instantiations Instance()--> (a 'Instance)
            if value[-2:]=='()': value = "(a '%s)"%value[:-2]
            #print "DEBUG4:",value
            output = '('+short_var_name + ' ' + value+')'
        elif cur_object_type == 'CondType':
            condition = cur_object_header
            # fix: rewrite "a in x.y.z" --> (member a (z (y x)))
            res = condition.split(' in ')
            if len(res)==2:
                xyz = res[1].split('.')
                xyz.reverse()
                for r in range(len(xyz)):
                    if r+1 == len(xyz):
                        xyz[r] = xyz[r]+')'*max(len(xyz)-1,0)
                    else:
                        xyz[r] = '('+xyz[r]
                xyz = ' '.join(xyz)
                condition = '(member '+res[0]+' '+xyz+')'
            if condition.strip(' ()')=='':
                output = '(else '+'\n'
            else:
                output = '(if ('+condition+')\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = '\n'.join(map(lambda x:indent+x,body_output.split('\n')))
            output += body_output+')'
        elif cur_object_type == 'LoopType':
            output = 'for '+cur_object_header[0]+' in '+cur_object_header[1]+':' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'FunctionType':
            # (defmethod <name> <argument list> ...<body>...)
            # creates a method or function
            # where <argument-list> is a list
            #   ((<argument name> <class of argument>) ...)

            method_name = self.local_name(cur_object_full_name)
            parent_name = self.local_name(self.parent(cur_object_full_name))
            method_arglist = '('+' '.join(['(self %s)'%parent_name]+map(lambda z:'(the_%s %s)'%(z,z),cur_object_header))+')'
            
            body_output = ''
            toplevel_output = ''
            for child_full_name in self.children(full_name):
                #print "DEBUG child_full_name",child_full_name,"self.children(full_name):",self.children(full_name),"full_name",full_name
                child_object = self.get_object_ptr(child_full_name)
                child_object_type = child_object[1]
                if child_object_type in ('FunctionType','ClassType'):
                    toplevel_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
                else: # goes into body 
                    body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = '\n'+'\n'.join(map(lambda x:indent+x,body_output.split('\n')))
            if not body_output.strip():
                body_output = ''
            toplevel_output = '\n'.join(map(lambda x:x,toplevel_output.split('\n')))
            if method_name == '__main__': # special case: don't display toplevel function for clisp
                output = toplevel_output
            else:
                output = '(defmethod %s %s (%s))\n%s'%(method_name,method_arglist,body_output,toplevel_output)
            output = output.strip()+'\n\n'
            
        elif cur_object_type == 'ClassType':
            # (defobject <name> <instance variables>
            #   <inherits from classes>)
            # creates a new class
            # where <instance variables>  is a list of
            #   ((<variable name> <default value>) (<var> <default>) ...)

            inheritance_string = '('+' '.join(cur_object_header)+')'
            name = self.local_name(cur_object_full_name)

            body_output = ''
            toplevel_output = ''
            for child_full_name in self.children(full_name):
                child_object = self.get_object_ptr(child_full_name)
                child_object_type = child_object[1]
                if child_object_type in ('FunctionType','ClassType'):
                    toplevel_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
                else: # goes into body 
                    body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = '\n'+'\n'.join(map(lambda x:indent+x,body_output.split('\n')))
            if not body_output.strip():
                body_output = ''
            toplevel_output = '\n'.join(map(lambda x:x,toplevel_output.split('\n')))
            output = '(defobject %s (%s) %s)\n%s'%(name,body_output,inheritance_string,toplevel_output)
            output = output.strip()+'\n\n'
            
        elif cur_object_type == 'ListType':
            name = self.local_name(cur_object_full_name)
            items = ' '.join(map(lambda x:"(a '%s)"%x,cur_object_header))
            output = "(%s (list (%s))"%(name,items)
        else:
            output = 'ERROR: Unknown type can\'t be rendered!'
        return output
        
    def render_code_python(self,full_name='__main__'):
        cur_flavor = 'python'
        indent = '     '
        # recursively generates the code below a given object
        cur_object = self.get_object_ptr(full_name)
        #print "DEBUG2",full_name,cur_object
        cur_object_full_name,cur_object_type,cur_object_header,cur_object_body = cur_object
        if cur_object_type == 'ExecutionType':
            # e.g. "pacman.eat(dot)" ==> [SOMEGENERATEDNAME,'ExecutionType',['pacman.eat','FunctionType',[arguments list]],[]]
            output = self.relativize_name(cur_object_header[0],cur_object_full_name)
            if cur_object_header[1]=='FunctionType':
                args = string.join(cur_object_header[2],', ')
                function_ending = '('+args+')'
                output += function_ending
        elif cur_object_type == 'DefinitionType':
            short_var_name = self.local_name(cur_object_full_name)
            value = cur_object_header[0]
            #print "DEBUG4:",value
            output = short_var_name + ' = ' + value
        elif cur_object_type == 'CondType':
            if cur_object_header.strip(' ()')=='':
                output = 'else: '+'\n'
            else:
                output = 'if '+cur_object_header+':' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'LoopType':
            output = 'for '+cur_object_header[0]+' in '+cur_object_header[1]+':' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'FunctionType':
            output = 'def '+self.local_name(cur_object_full_name)+'('+string.join(cur_object_header,', ')+'):' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                #print "DEBUG child_full_name",child_full_name,"self.children(full_name):",self.children(full_name),"full_name",full_name
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            if not body_output:
                body_output = 'pass'+'\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'ClassType':
            if len(cur_object_header) > 0:
                inheritance_string = '('+string.join(cur_object_header,', ')+')'
            else:
                inheritance_string = ''
            output = 'class '+self.local_name(cur_object_full_name)+inheritance_string+':' + '\n'
            body_output = ''
            for child_full_name in self.children(full_name):
                body_output += self.render_code(child_full_name,flavor=cur_flavor) + '\n'
            if not  body_output:
                body_output += 'pass'+'\n'
            body_output = string.join(map(lambda x:indent+x,body_output.split('\n')),'\n')
            output += body_output
        elif cur_object_type == 'ListType':
            output = self.local_name(cur_object_full_name) + ' = ['+string.join(cur_object_header,', ')+']'
        else:
            output = 'ERROR: Unknown type can\'t be rendered!'
        return output
            

    def children(self,parent_full_name):
        # returns a list of the full_names of the children, if any
        parent_object = self.get_object_ptr(parent_full_name)
        parent_object_children = parent_object[3]
        children_full_names = map(lambda x:x[0],parent_object_children)
        #print "DEBUG3",children_full_names
        return children_full_names
        
    def parent(self,full_name):
        # returns the string for the parent object's full name
        # assumes full_name is in standard dotted notation
        steps = full_name.split('.')
        steps_one_level_up = steps[:-1]
        parent_name = string.join(steps_one_level_up,'.')
        return parent_name

    def dir(self,parent_full_name='__auto__'):
        if parent_full_name=='__auto__': # then assume the current scope is the parent
            parent_full_name = self.focus[:]    
        # lists all the full names in this namespace
        parent_ptr = self.get_object_ptr(parent_full_name)
        print "PARENT_PTR",parent_ptr
        if parent_ptr[1]=='FunctionType':
            args = parent_ptr[2]
            args_full_names = map(lambda x:parent_full_name+'.'+x,args)
        else:
            args_full_names = []
        children_nodes_ptr = parent_ptr[3]
        childrens_full_names = map(lambda x:x[0],children_nodes_ptr)
        return childrens_full_names+args_full_names

    def new_list_object(self,list_full_name,list_contents):
        # list_contents is a list of string objects,
        # python numbers or strings need to be wrapped
        return self.new_object(list_full_name,'ListType',list_contents,[])
    
    def new_loop_object(self,parent_full_name,iteration_var_full_name,list_to_loop_over_full_name):
        # need to generate name for loop
        nonce = 'LOOP_'+string.join(map(lambda x:random.choice(string.letters),[None]*7),'')
        loop_full_name = parent_full_name+'.'+nonce
        return self.new_object(loop_full_name,'LoopType',[iteration_var_full_name,list_to_loop_over_full_name],[])

    def new_class_object(self,class_full_name,inheritance_list):
        return self.new_object(class_full_name,'ClassType',inheritance_list,[])
    
    def new_function_object(self,function_full_name,argument_list):
        return self.new_object(function_full_name,'FunctionType',argument_list,[])

    def new_cond_object(self,parent_full_name,cond_string):
        # if the cond_string is empty, assume it is an else
        nonce = 'COND_'+string.join(map(lambda x:random.choice(string.letters),[None]*7),'')
        cond_full_name = parent_full_name+'.'+nonce
        return self.new_object(cond_full_name,'CondType',cond_string,[])

    def new_execution_object(self,parent_full_name,to_execute_full_name,execution_type,execution_args_list):
        nonce = 'EXEC_'+string.join(map(lambda x:random.choice(string.letters),[None]*7),'')
        execution_full_name = parent_full_name+'.'+nonce
        return self.new_object(execution_full_name,'ExecutionType',[to_execute_full_name,execution_type,execution_args_list],[])
    
    def new_definition_object(self,target_var_full_name,source_string):
        # e.g.  target_variable = source_string
        # put value in header
        return self.new_object(target_var_full_name,'DefinitionType',[source_string],[])
                          
    def new_object(self,full_name,type,header,body):
        # the header is a object-type-specific thing
        # the body is always a list of the ordered child objects (i.e. lines)
        return [full_name,type,header,body]

    def replace_object(self,full_name,replacement_object):
        object_ptr = self.get_object_ptr(full_name)
        if object_ptr:
            object_ptr[0] = replacement_object[0]
            object_ptr[1] = replacement_object[1]
            object_ptr[2] = replacement_object[2]
            object_ptr[3] = replacement_object[3]
        return

    def append_object_body(self,full_name,object_to_append):
        object_ptr = self.get_object_ptr(full_name)
        if object_ptr:
            object_ptr[3] = object_ptr[3]+[object_to_append]
        return

    def add_object(self,child_object):
        full_name = child_object[0]
        parent_full_name = self.parent(full_name)
        #print "DEBUG5",full_name,parent_full_name
        # stores it inside its parent object
        parent_object_ptr = self.get_object_ptr(parent_full_name)
        print "DEBUG add object",parent_object_ptr," : ",parent_full_name," : ", child_object
	if parent_object_ptr == None:
	    print "Error empty parent object"
        parent_contents_ptr = parent_object_ptr[3]
        parent_contents_ptr.append(child_object)
        return

    def get_object_ptr(self,full_name):
        # searches for full_name in self.objects tree
        search_queue = self.objects[:]
        while len(search_queue)>0:
            node_to_examine = search_queue[0]
            #print "DEBUG",full_name,node_to_examine
            node_to_examine_name,node_to_examine_type,node_to_examine_header,node_to_examine_body = node_to_examine
            if node_to_examine_name == full_name:
                return node_to_examine # found it!
            # otherwise, expand this node onto search queue
            del search_queue[0]
            children_nodes = node_to_examine_body
            search_queue += children_nodes
        # not found
        return None

        
        
