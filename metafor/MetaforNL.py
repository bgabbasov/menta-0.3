# NL Library for Metafor
#
#
# pacman example:
# the yellow dots are set through a maze and
# pacman, the chomping yellow circle, has to collect them.
# There are blinking big yellow dots that
# allow you to eat the ghosts
#
# prediscourse understanding:
#  dots are thing or yellow dots are thing?
#  set(yellow_dots,through a maze) ==> what does it met to set the yellow dots through a maze?
#  maze ==> object
#  pacman ==> object
#   pacman appositive, the chomping yellow circle
#     circle, yellow ==> attributes of pacman
#     chomp ==> ability of pacman
#  them ==> yellow dots
#  collect(pacman,yellow_dots)
#  be(there, blinking big yellow dots)
#  blinking big yellow dots ==> you-->eat(ghosts)
#
#
# problem: the expression: "blinking yellow dots"
#  can map to:
#  1) class blinking_yellow_dots
#  2) [class blinking_yellow_dot,...]
#  3) class dot: color=yellow type=blinking
#  4) class dot: color=yellow, def blink()
#  etc...

import os, string, re, random, time
from montylingua import MontyLingua
from types import *
import logging

class MetaforNL:

    def __init__(self,metafor_handle):
        self.ml = MontyLingua.MontyLingua()
        self.m = metafor_handle
        self.lookup = {}
        self.deictic_stack = [] # entry: [('Pacman',('he','singular')),...]
        self.questions_queue = [] # if active, active_question = {'!question':'Can x do y?','!question_asked':0,'!question_requires_answer_p':1,'yes'(possible responses):['actions to do',...],'no':['actions to do',...]}
        

    def process(self,query):
        # were we expecting a response? (check if questions_queue is active
        if self.questions_queue and self.questions_queue[0]['!question_asked'] and self.questions_queue[0]['!question_requires_answer']:
            response_or_followup_question = self.process_response(query)
            return response_or_followup_question
        # preprocess: recognize quotes
        preprocessed_query = self.recognize_quotes(query)
        # preprocess: lists
        preprocessed_query = self.recognize_lists(preprocessed_query)
        # preprocess: recognise scoping statements
        preprocessed_query = self.resolve_scoping_statements(preprocessed_query)
        print "DEBUG scoping resolved to:\n",preprocessed_query
        # preprocess: recognise conditionals
        preprocessed_query = self.resolve_cond_statements(preprocessed_query)
        print "DEBUG conditionals resolved to:\n",preprocessed_query
        # logging.debug("conditionals resolved to:\n " + preprocessed_query)
        sentence_digests = self.ml.jist(preprocessed_query)
        sentences_and_their_pps = map(lambda x:x['parameterized_predicates'],sentence_digests)
        # collapse each sentence's pps into a single stream of pps
        sequence_of_pps_ptr = reduce(lambda x,y:x+y,sentences_and_their_pps)
        # resolve deixis
        self.process_deixis(sequence_of_pps_ptr)
        # resolve complementizers (e.g. who, that)
        self.resolve_complementizers(sequence_of_pps_ptr)
        # https://github.com/menta/menta-0.3/issues/20 Demo: extend analysis to process problem description.
        print "DEBUG sequence of pps",'\n'.join(map(str,sequence_of_pps_ptr))
        responses = []
        for cur_index in range(len(sequence_of_pps_ptr)):
            response = self.process_pp(sequence_of_pps_ptr,cur_index)
            responses.append(response)
        return string.join(responses,'  ')

    def process_deixis(self,pp_list_ptr):
        # resolve each pp against deictic stack
        # and update deictic stack with new entries
        male_fnames = ['Hugo','Push','Marvin','Nick','James','Jim','John','Johnny','Robert','Bob','Michael','Mike','William','Bill','Billy','David','Dave','Richard','Dick','Charles','Charlie','Joseph','Joe','Joey','Thomas','Tom','Tommy','Christopher','Chris','Daniel','Dan','Paul','Mark','Donald','Don','George','Kenneth','Ken','Steven','Stephen','Steve','Edward','Eddie','Ed','Brian','Ronald','Ron','Anthony','Tony','Kevin','Jason','Matthew','Matt','Gary','Timothy','Tim','Jose','Larry','Jeffrey','Jeff','Frank','Fred','Scott','Eric','Stephen','Andrew','Andy','Raymond','Ray','Gregory','Greg','Gregg','Joshua','Josh','Jerry','Dennis','Walter','Patrick','Pat','Peter','Harold','Harry','Douglas','Henry','Carl','Arthur','Ryan','Roger','Sam','Dwight','Melvin','Juan']
        female_fnames = ['Briana','Lea','Eileen','Belinda','Juanita','Julie','Sally','Cindy','Jane','Joyce','Judy','Alyssa','Mary','Patricia','Patty','Linda','Barbara','Elizabeth','Jennifer','Maria','Susan','Margaret','Dorothy','Lisa','Nancy','Karen','Betty','Helen','Sandra','Donna','Carol','Ruth','Sharon','Michelle','Laura','Laurie','Sarah','Sara','Kimberly','Kim','Deborah','Jesse','Jessica','Shirley','Cynthia','Angela','Angie','Melissa','Brenda','Amy','Anna','Rebecca','Becky','Virginia','Kathleen','Kathy','Pamela','Martha','Debra','Amanda','Stephanie','Carolyn','Carol','Christine','Marie','Janet','Catherine','Cathy','Frances','Ann','Annie','Diane','Diana','Dianna']
        common_agents = ['bartender','milkman','pacman','customer','boss']
        stop_words = ['there','that','one','which']
        key_words = ['LIST','QUOTE','ANTECEDENT','SCOPE']
        
        for i in range(len(pp_list_ptr)):
            pp = pp_list_ptr[i]
            # syntactic parse of predicate
            verb,verb_features = pp[0]
            subj,subj_features = pp[1]
            objs = map(lambda x:x[0],pp[2:])
            objs_features = map(lambda x:x[1],pp[2:])
            obj_count = len(objs)
            # resolve it,he,she,him,her,them,they
            pronouns = ['it','he','she','him','her','them','they','whom','who','one']
            if subj.lower() in pronouns:
                the_range = range(len(self.deictic_stack))
                the_range.reverse()
                the_range = the_range[:6] # trim to recent six
                for j in the_range:
                    candidate_referent,candidate_pronouns = self.deictic_stack[j]
                    if subj.lower() in candidate_pronouns: # found!
                        pp_list_ptr[i][1][0]=candidate_referent # resolve referent!
                        break
            for k in range(obj_count):
                obj = objs[k]
                if obj.lower() in pronouns: # direct object case
                    the_range = range(len(self.deictic_stack))
                    the_range.reverse()
                    the_range = the_range[:6] # trim to recent six
                    for j in the_range:
                        candidate_referent,candidate_pronouns = self.deictic_stack[j]
                        if obj.lower() in candidate_pronouns: # found!
                            pp_list_ptr[i][k+2][0]=candidate_referent # resolve referent!
                            break
                elif 'prep=' in map(lambda x:x[:5],objs_features[k]) and len(obj.split())>=2 and obj.split()[1].lower() in pronouns: # indirect obj
                    the_prep = objs_features[k][map(lambda x:x[:5],objs_features[k]).index('prep=')].split('=')[1]
                    the_range = range(len(self.deictic_stack))
                    the_range.reverse()
                    the_range = the_range[:6] # trim to recent six
                    for j in the_range:
                        candidate_referent,candidate_pronouns = self.deictic_stack[j]
                        if obj.split()[1].lower() in candidate_pronouns: # found!
                            pp_list_ptr[i][k+2][0]=the_prep+' '+candidate_referent # resolve referent!
                            break
            # now update the deictic stack
            candidates = [(subj,subj_features)]
            for k in range(len(objs)):
                if 'prep=' not in map(lambda x:x[:5],objs_features[k]):
                    candidates.append((objs[k],objs_features[k]))
                elif len(objs[k].split())>=2:
                    candidates.append((' '.join(objs[k].split()[1:]),objs_features[k])) # NP nested in PP
            candidates = filter(lambda x:x[0].lower() not in pronouns and x[0].strip()!='',candidates)
            for m in range(len(candidates)):
                phrase,its_features = candidates[m]
                annotations = []
                # is it plural?
                if 'determiner=some' in its_features or 'plural' in its_features:
                    # and allow "one" to refer to them in the singular if they are agent
                    if phrase in common_agents:
                        self.deictic_stack.append((phrase,['one']))
                    annotations+=['they','them']
                    phrase = phrase+'s' # pluralize the lemma                    
                elif (phrase[0].isupper() and phrase.lower() not in stop_words and phrase.split('_')[0] not in key_words) or phrase.lower() in common_agents: # means it is an agent
                    # is the gender known?
                    if phrase in male_fnames:
                        annotations+=['he','him','his','who']
                    elif phrase in female_fnames:
                        annotations+=['her','she','hers','who']
                    else:
                        annotations+=['he','him','his','her','she','hers','who']
                elif (phrase.lower() not in stop_words and phrase.split('_')[0] not in key_words): # otherwise it is a thing
                    annotations+=['it']
                else:
                    continue
                self.deictic_stack.append((phrase,annotations))
        return
        
    def resolve_cond_statements(self,text):
        # e.g. if BLAH, (then) BLAH. or
        #      BLAH if BLAH. or
        #      (otherwise|or else) BLAH.
        # ==> pps: (metafor_cond_begin ANTECEDENT "") (make bartender drink) (give "" customer drink) (metafor_cond_end "" "")
        sentences = map(lambda x:x.strip(),self.ml.split_sentences(text))
        # actually, let sentences here mean independent clauses!
        # that way, a when... can scope over clause1; clause2
        sentences = map(lambda x:map(lambda y:y.strip(),x.split('; ')),sentences)
        sentences = reduce(lambda x,y:x+y,sentences,[])
        print "DEBUG INDEP CLAUSES",sentences
        for i in range(len(sentences)):
            m1 = re.search('^(ifever|Ifever|if|If|only if|Only if) (?P<antecedentphrase>[a-zA-Z][^,]+), (then |)(?P<consequentphrase>.+$)',sentences[i].strip())
            m2 = re.search('^(?P<consequentphrase>.+) (ifever|Ifever|if|If) (?P<antecedentphrase>[a-zA-Z].+$)',sentences[i].strip())
            m3 = re.search('^(otherwise|Otherwise|Or else|or else|Else|else)(,|) (?P<antecedentphrase>)(?P<consequentphrase>.+$)',sentences[i].strip())
            if len(filter(lambda x:x!=None,(m1,m2,m3)))==0:
                continue
            m = filter(lambda x:x!=None,(m1,m2,m3))[0]
            antecedent = m.group('antecedentphrase').strip(' .!?;')
            consequent = m.group('consequentphrase').strip(' .!?;')
            print "DEBUGA",antecedent,consequent
            # DO NOT RESOLVE ANTECEDENT HERE
            new_antecedent_key = 'ANTECEDENT_'+string.join(map(lambda x:random.choice(string.letters),[None]*10),'')
            self.lookup[new_antecedent_key] = antecedent
            sentences[i] = 'metafor_cond_begin '+new_antecedent_key+' .  '+consequent.strip('. ')+' . metafor_cond_end . '
        return ' '.join(sentences)
                
    def normalize_nlphrase(self,phrase):
        # tags, removes DT MD
        # and lemmatizes
        tagged = self.ml.tag_tokenized(self.ml.tokenize(phrase))
        tagged = self.filter_by_tag(tagged,blacklist=('DT','MD'),whitelist=())
        lemmatized = self.ml.lemmatise_tagged(tagged)
        return ' '.join(map(lambda x:x.split('/')[2],lemmatized.split()))
        
    def resolve_scoping_statements(self,text):
        # e.g. "when pacman runs" or "when pacman eats dots"
        # ==> pps: (examine "" __main__.pacman) .....all other pps.... (examine "" __main__)
        # this is a scoping wrapper
        sentences = map(lambda x:x.strip(),self.ml.split_sentences(text))
        print "DEBUG sentences",sentences
        for j in range(len(sentences)):
            m = re.search('^(when|whenever|When|Whenever|As|as) (?P<scopingphrase>[a-zA-Z][^,]+),(?P<scopedphrase>.+$)',sentences[j].strip())
            if m:
                scope_phrase = m.group('scopingphrase')
                # parse the SVO of the scope phrase
                sentence_digests = self.ml.jist(scope_phrase)
                sentences_and_their_pps = map(lambda x:x['parameterized_predicates'],sentence_digests)
                # collapse each sentence's pps into a single stream of pps
                sequence_of_pps_ptr = reduce(lambda x,y:x+y,sentences_and_their_pps)
                # there should only be one pp...so take the first (if there aren't any, skip this sentence)
                self.process_deixis(sequence_of_pps_ptr) # also, first resolve the deixis
                if len(sequence_of_pps_ptr) == 0:
                    continue
                pp = sequence_of_pps_ptr[0]
                # syntactic parse of predicate
                verb,verb_features = pp[0]
                verb_escaped = self.escape_phrase(verb)
                subj,subj_features = pp[1]
                subj_escaped = self.escape_phrase(subj)
                objs = map(lambda x:x[0],pp[2:])
                objs_features = map(lambda x:x[1],pp[2:])
                objs_escaped = map(self.escape_phrase,objs)
                obj_count = len(objs)
                # verb: method, subj: class, obj(optional): argument to class
                if not self.m.resolve_name(subj_escaped): # if subj not yet classified, do so
                    new_object = self.m.new_class_object(self.m.focus+'.'+subj_escaped,[])
                    self.m.add_object(new_object)
                # if function not yet declared, do so
                if not (self.m.resolve_name(subj_escaped+'.'+verb_escaped) and self.m.type(self.m.resolve_name(subj_escaped+'.'+verb_escaped))=='FunctionType'): 
                    new_function_full_name = self.m.focus+'.'+subj_escaped+'.'+verb_escaped
                    new_function_object = self.m.new_function_object(new_function_full_name,[])
                    self.m.add_object(new_function_object)
                # do arguments
                arguments = []
                arguments_plaintext = []
                for i in range(len(objs)):
                    arguments.append(objs_escaped[i])
                    arguments_plaintext.append(objs[i])
                if arguments:
                    # replace the arguments field in the new function
                    function_object_ptr = self.m.get_object_ptr(self.m.resolve_name(subj_escaped+'.'+verb_escaped))
                    print function_object_ptr
                    function_object_ptr[2] = arguments
                # finally, do scoping
                # ok! this scope is complete enough to act on!
                new_focus = self.m.resolve_name(subj_escaped+'.'+verb_escaped)
                new_focus_key = 'SCOPE_'+string.join(map(lambda x:random.choice(string.letters),[None]*10),'')
                self.lookup[new_focus_key] = new_focus
                scope_begin_expression = 'metafor_scope_begin '+new_focus_key
                scope_end_expression = 'metafor_scope_end '+new_focus_key
                # now update the sentence
                sentences[j] = scope_begin_expression + ' . ' +m.group('scopedphrase').strip('. ')+' . ' + scope_end_expression +' .  '
        # reconnect sentences
        output_text = string.join(sentences,' ')
        return output_text
        
    def resolve_complementizers(self,pp_list_ptr):
        for i in range(len(pp_list_ptr)):
            pp = pp_list_ptr[i]
            # syntactic parse of predicate
            verb,verb_features = pp[0]
            verb_escaped = self.escape_phrase(verb)
            subj,subj_features = pp[1]
            subj_escaped = self.escape_phrase(subj)
            objs = map(lambda x:x[0],pp[2:])
            objs_features = map(lambda x:x[1],pp[2:])
            objs_escaped = map(self.escape_phrase,objs)
            obj_count = len(objs)
            # look for 'who'/'that' as subjects
            if i>=1 and subj in ['who','whom','that','which',''] and verb[:len('metafor_')]!='metafor_' and pp_list_ptr[i-1][0][0][:len('metafor_')]!='metafor_':
                pp_prev = pp_list_ptr[i-1]
                subj_prev,subj_prev_features = pp_prev[1]
                verb_prev,verb_features_prev = pp_prev[0]
                if subj_prev.lower() not in ['who','whom','that','which','','there','it']  and verb_prev not in ["have","contain","include"]:
                    # if prev verb is containment, then
                    # referent is the prevObj, not preSubj
                    # e.g. "The bar has a menu which contains"
                    #
                    # '*' at the end of the phrase denotes that it is a resolved entity, but we will allow this
                    # if prev subject was a resolved entity, then use direct object instead
                    pp[1][0] = subj_prev.strip('*')+'*' # resolved!
                elif subj_prev.lower() not in ['who','whom','that','which','','there','it'] and not (len(subj_prev)>0 and subj_prev[-1]=='*') and verb_prev in ["have","contain","include"]:
                    obj1_prev,obj1_prev_features = pp_prev[2]
                    # e.g. game has a score which contains
                    # resolve to game 's score contains
                    pp[1][0] = subj_prev+' \'s '+obj1_prev.strip('*')+'*'
                    
                elif len(pp_prev)>=3: # there is a direct object
                    obj1_prev,obj1_prev_features = pp_prev[2] # resolved!
                    pp[1][0] = obj1_prev.strip('*')+'*'
        # remove '*' from anaphors
        for i in range(len(pp_list_ptr)):
            pp = pp_list_ptr[i]
            map(lambda i:pp[i].__setitem__(0,pp[i][0].strip(' *')),range(len(pp)))
            
        return
        
    def process_pp(self,pp_list_ptr,cur_index):
        print("process_pp started")
        pp = pp_list_ptr[cur_index]
        
        # syntactic parse of predicate
        print "DEBUG process_pp ", pp
        # Request case:
        if(pp[1][0] == None or pp[1][0] == '' or pp[1][0].lower() == 'please') :
            pp[1] = [self.m.selfReference, []]
         
        subj,subj_features = pp[1]
        print ("DEBUG process_pp ", pp)
        verb,verb_features = pp[0]
        verb_escaped = self.escape_phrase(verb)        
        subj_escaped = self.escape_phrase(subj)
        objs = map(lambda x:x[0],pp[2:])
        objs_features = map(lambda x:x[1],pp[2:])
        objs_escaped = map(self.escape_phrase,objs)
        objs_normalized = map(self.normalize_execution_arg,objs_escaped)
        obj_count = len(objs)

        # define synsets
        ss_reserved_verbs = ['be','have']
        ss_be = ['be']
        ss_have = ['have','contain','include','associate']
        ss_there = ['there','There']
        
        # recognize what's defined
        print 'context: ',self.m.get_context()
        # 6) e.g. (context: procedural, like inside a function) pacman scores a point
        if self.m.get_context()=='procedural' and (verb not in ss_reserved_verbs) and self.m.resolve_name(subj_escaped):
            objs_decoded = map(self.normalize_execution_arg,objs_escaped)
            objs_typed = map(self.generalize_phrase,objs_escaped)
            output = "ok."
            # lookup verb
            the_verb_fullname = self.m.resolve_name(subj_escaped)+'.'+verb_escaped
            print "DEBUG the verb fullname",the_verb_fullname
            if not self.m.fullname_exists_p(the_verb_fullname):
                new_function_full_name = the_verb_fullname
                new_function_object = self.m.new_function_object(new_function_full_name,objs_typed)
                self.m.add_object(new_function_object)
            elif self.m.type(the_verb_fullname) != 'FunctionType':
                # make the verb in a function first
                # TODO
                pass
            # now form the execution statement object
            exec_obj = self.m.new_execution_object(self.m.focus,subj_escaped+'.'+verb_escaped,'FunctionType',objs_decoded)
            # now append this object to the end of the current object
            self.m.append_object_body(self.m.focus,exec_obj)
            output += "  i processed that action."
            return output                
        # 5) e.g. metafor_scope_begin SCOPE_asASDFaew
        #    i.e. resolve scoping statements which sets the current focus
        elif (verb in ['metafor_scope_begin','metafor_scope_end']) and len(objs)>=1:
            output = "ok."
            scope = self.lookup[objs[0]]
            if verb == 'metafor_scope_begin':
                output += "  now we are going to think about "+scope+"..."
                # push the current focus on stack
                self.m.focus_stack.append(self.m.focus)
                # change the focus
                self.m.focus = scope
            elif verb == 'metafor_scope_end':
                # pop the stack
                self.m.focus = self.m.focus_stack.pop()
                output += "  now that we are done thinking about "+scope+", we are going to resume thinking about "+self.m.focus+"."
            return output
        # 8) e.g. metafor_cond_begin COND_asdfasdf
        #    i.e. set current focus to new cond object
        elif (verb in ['metafor_cond_begin','metafor_cond_end']):
            output = "ok."
            if verb == 'metafor_cond_begin':
                antecedent = self.lookup[objs[0]]
                # now resolve the antecedent
                # we know a few comparators:
                # is less than, is greater than, is in, is PROPERTY
                # is NP (equality), is equal to
                # also partition by NOT and AND and OR
                # but now we must break the language barrier :(
                bool_toks = re.split('(and|or)',antecedent)
                valid_operator_mappings = {
                    'is less than or equal to':'<=',
                    'is greater than or equal to':'>=',
                    'is less than':'<',
                    'is great than':'>',
                    'is not equal to':'!=',
                    'is equal to':'==',
                    'has the same value as':'==',
                    'is the same as':'==',
                    'is not':'!=',
                    'is in':'in',
                    'is not in':'not in',
                    'is':'=='}
                for j in range(len(bool_toks)):
                    phrase = bool_toks[j]
                    if phrase in ['and','or']:
                        continue
                    valid_splits = valid_operator_mappings.keys()
                    valid_splits.sort()
                    valid_splits.reverse()
                    valid_splits = '('+'|'.join(valid_splits)+')'
                    phrase_toks = re.split(valid_splits,phrase)
                    if len(phrase_toks)!=3: # not recognized
                        continue
                    car,the_operator,cdr=phrase_toks
                    car = self.normalize_nlphrase(car)
                    cdr = self.normalize_nlphrase(cdr)
                    car = self.m.resolve_name(self.escape_phrase(car))
                    print "CDR",cdr
                    cdrs = filter(lambda x:x.strip()!='',[self.m.resolve_name(self.escape_phrase(cdr+'s')),self.m.resolve_name(self.escape_phrase(cdr))])
                    print cdrs
                    if len(cdrs)==0:
                        continue
                    cdr = cdrs[0]
                    car,cdr = map(lambda x:self.m.relativize_name(x,self.m.focus),(car,cdr))
                    bool_toks[j] = car+' '+valid_operator_mappings[the_operator]+' '+cdr
                complete_antecedent = ' '.join(map(lambda x:'('+x+')',bool_toks))
            
                new_object = self.m.new_cond_object(self.m.focus,complete_antecedent)
                self.m.add_object(new_object)
                name_of_cond_scope = new_object[0]
                # push the current focus on stack
                self.m.focus_stack.append(self.m.focus)
                # change focus
                self.m.focus = name_of_cond_scope
            elif verb == 'metafor_cond_end':
                self.m.focus = self.m.focus_stack.pop()
            return output
        
        # 4) e.g. PACMAN is a character ==> be(class,superclass)
        #    unless PACMAN is a list of ___
        elif (verb in ss_be) and (subj not in ss_there+['']) and len(objs)>=1:
            output = "ok."
            # is subj a known thing?  if not, make it so
            if not self.m.resolve_name(subj_escaped):
                new_object = self.m.new_class_object(self.m.focus+'.'+subj_escaped,[objs_escaped[0]])
                self.m.add_object(new_object)
                output += "  i created a new agent "+subj+" that is a kind of "+objs[0]+" agent."
            else:
                # if already known, is it a class?  if not, make it so
                if self.m.type(self.m.resolve_name(subj_escaped))!='ClassType':
                    new_object = self.m.new_class_object(self.m.focus+'.'+subj_escaped,[objs_escaped[0]])
                    self.m.replace_object(self.m.resolve_name(subj_escaped),new_object)
                    output += "  i changed "+subj+" into an agent, that is a kind of agent called "+objs[0]+"."
                else: # so it is a class already.. make sure that character is in the inheritance list
                    object_ptr = self.m.get_object_ptr(self.m.resolve_name(subj_escaped))
                    if objs_escaped[0] not in object_ptr[2]:
                        object_ptr[2].append(objs_escaped[0])
                        output += "  i made the "+subj+" agent a kind of the agent called "+objs[0]+"."
            return output
                                                         
        # 7) e.g. DRINKS INCLUDES LIST_asdwqer ||
        #         DRINKS INCLUDES MARTINI
        #    i.e. DRINKS = [foo,bar]
        #    have to instantiate object for each member
        elif (verb in ss_have) and (self.m.resolve_name(subj_escaped+'s')) and self.m.type(self.m.resolve_name(subj_escaped+'s'))=='ListType' and len(objs) >= 1:
            output = "ok."
            known_thing_full_name = self.m.resolve_name(subj_escaped+'s')
            known_thing_local_name = self.m.local_name(known_thing_full_name)
            known_thing_local_name_singular = self.m.local_name(known_thing_full_name)[:-1]
            if objs[0][:len('LIST_')]=='LIST_':
                the_list = self.lookup[objs[0]]
            else: # make a list!
                the_list = [objs[0]]
                
            # first, instantiate every item in list as class
            # and inherit from the type of the list (drink)
            for an_item in the_list:
                an_item_escaped = self.escape_phrase(an_item)
                if not self.m.resolve_name(an_item_escaped):
                    new_object = self.m.new_class_object(self.m.top_level_focus+'.'+an_item_escaped,[known_thing_local_name_singular])
                    self.m.add_object(new_object)
                    output += "  i created a new object called "+an_item+'.'
            # second, append to the list object
            list_object_ptr = self.m.get_object_ptr(known_thing_full_name)
            list_object_ptr[2]+=map(lambda x:self.escape_phrase(x),the_list)
            output += "  i added "+', '.join(map(lambda x:self.escape_phrase(x)+'()',the_list))+' to the '+known_thing_local_name+'s'+' list.'
            return output
        
        # 3) e.g. PACMAN has a color / PACMAN has some sizes
        #    i.e. have(KNOWN_THING/CLASS,direct_object)
        elif (verb in ss_have) and (self.m.resolve_name(subj_escaped)) and len(objs) >= 1 and ('prep=' not in map(lambda x:x[:5],objs_features[0])):
            output = "ok."
            known_thing_full_name = self.m.resolve_name(subj_escaped)
            if self.m.type(known_thing_full_name) != 'ClassType': # if not a class yet, cast it
                known_thing_cast_to_class_object = self.m.new_class_object(known_thing_full_name,[])
                self.m.replace_object(known_thing_full_name,known_thing_cast_to_class_object)
                output += "  i changed "+subj+" into an agent."

            # is thing singular or plural?
            if ('determiner=a' not in objs_features[0] and 'determiner=an' not in objs_features[0]) and 'determiner=some' in objs_features[0] or 'plural' in objs_features[0]: # plural
                if not self.m.resolve_name(subj_escaped+'.'+objs_escaped[0]+'s'):
                    # add a new list member object
                    new_full_name = self.m.focus+'.'+subj_escaped+'.'+objs_escaped[0]+'s'
                    new_object = self.m.new_list_object(new_full_name,[])
                    self.m.add_object(new_object)
                output += "  i augmented "+subj+" with the member: "+objs[0]+"s"+"."
            else: # singular 
                if not self.m.resolve_name(subj_escaped+'.'+objs_escaped[0]):
                    local_instance_name = 'the_'+objs_escaped[0]
                    new_definition_full_name = self.m.focus+'.'+subj_escaped+'.'+local_instance_name
                    new_definition_object = self.m.new_definition_object(new_definition_full_name,objs_escaped[0]+'()')
                    self.m.add_object(new_definition_object)
                    output += "  i augmented "+subj+" with the property: "+objs[0]+"."
            # also, make a class object on the outside if it doesn't already exist
            if (self.m.resolve_name(objs_escaped[0]) not in self.m.dir()):
                self.m.add_object(self.m.new_class_object(self.m.focus+'.'+objs_escaped[0],[]))
                output += "  i created an object called "+objs[0]+" within "+self.m.local_name(self.m.focus)+'.'
            else:
                # ok, it does exist, but is it classtype? if not, recast it
                if self.m.type(self.m.resolve_name(objs_escaped[0]))!='ClassType':
                    self.m.replace_object(self.m.resolve_name(objs_escaped[0]),self.m.new_class_object(self.m.focus+'.'+objs_escaped[0],[]))
                    output += "  i change the object "+objs[0]+" into an agent, within "+self.m.local_name(self.m.focus)+'.'
            return output
            
        # 2) e.g. PACMAN eats dots / PACMAN can eat / there is a way for PACMAN to eat dots
        #    i.e. verb_not_passive(KNOWN_THING,optional object,optional object)
        elif (verb not in ss_reserved_verbs) and ('passive_voice' not in verb_features):# and (self.m.resolve_name(subj_escaped)):
            output = "ok."
            known_thing_full_name = self.m.resolve_name(subj_escaped)
            # HANDLE CLASS CREATION/UPDATE
            if not known_thing_full_name:
                # only create classes at top level!
                new_object = self.m.new_class_object(self.m.top_level_focus+'.'+subj_escaped,[])
                self.m.add_object(new_object)
                output += "  i created a new agent called "+subj+'.'
            elif self.m.type(known_thing_full_name) != 'ClassType': # if not a class yet, cast it
                known_thing_cast_to_class_object = self.m.new_class_object(known_thing_full_name,[])
                self.m.replace_object(known_thing_full_name,known_thing_cast_to_class_object)
                output += "  i changed "+subj+" into an agent."
            # HANDLE METHOD CREATION/UPDATE
            # now add the verb as a method if it doesn't already exist
            if self.m.type(self.m.resolve_name(subj_escaped+'.'+verb_escaped)) != 'FunctionType':
                new_function_full_name = self.m.resolve_name(subj_escaped)+'.'+verb_escaped
                new_function_object = self.m.new_function_object(new_function_full_name,[])
                self.m.add_object(new_function_object)
                output += "  i added the ability for "+subj+" to "+verb+"."
            # now check to see if there are optional arguments
            arguments = []
            arguments_plaintext = []
            for i in range(len(objs)):
                arguments.append(objs_normalized[i])
                arguments_plaintext.append(objs[i])
            if arguments:
                # replace the arguments field in the new function
                function_object_ptr = self.m.get_object_ptr(self.m.resolve_name(subj_escaped+'.'+verb_escaped))
                function_object_ptr[2] = arguments
                output += "  the "+subj+" can "+verb+" using "+string.join(arguments_plaintext,' and ')+"."
            return output            
        # 2) e.g. PACMAN is named John
        #    i.e. verb_passive(KNOWN_THING,1 direct object required)
        elif (verb not in ss_reserved_verbs) and ('passive_voice' in verb_features) and len(objs)==1 and 'prep=' not in map(lambda x:x[:len('prep=')],objs_features):
            output = "ok."
            known_thing_full_name = self.m.resolve_name(subj_escaped)
            if not known_thing_full_name:
                new_object = self.m.new_class_object(self.m.focus+'.'+subj_escaped,[])
                self.m.add_object(new_object)
                output += "  i created a new agent called "+subj+'.'
                known_thing_full_name = self.m.resolve_name(subj_escaped) # update
            elif self.m.type(known_thing_full_name) != 'ClassType': # if not a class yet, cast it
                known_thing_cast_to_class_object = self.m.new_class_object(known_thing_full_name,[])
                self.m.replace_object(known_thing_full_name,known_thing_cast_to_class_object)
                output += "  i changed "+subj+" into an agent."
            # now add the member variable if it doesn't already exist
            if self.m.resolve_name(subj_escaped+'.'+verb_escaped) not in self.m.dir(known_thing_full_name):
                new_variable_full_name = self.m.focus+'.'+subj_escaped+'.'+verb_escaped
                new_variable_object = self.m.new_definition_object(new_variable_full_name,objs_escaped[0])
                self.m.add_object(new_variable_object)
                output += "  i added a field called "+objs[0]+" to "+subj+'.'
            return output            
        # 1) e.g. there is a PACMAN /
        #         there are blinking big yellow dots /
        #         there is a PACMAN in the maze (location)
        #         there is a PACMAN with a mouth 
        #    i.e. be(there,THING[singular/plural])
        elif obj_count >= 1 and (verb in ss_be) and (subj in ss_there) and 'prep=' not in map(lambda x:x[:5],objs_features[0]):
            output = "ok. "
            where_to_put = self.m.focus
            # is there a container (e.g. there is a pacman IN THE MAZE)?
            if obj_count >= 2 and ('prep=in' in objs_features[1]):
                # does container exist? if not make it so
                if not self.m.resolve_name(objs_normalized[1]):
                    self.m.add_object(self.m.new_class_object(self.m.focus+'.'+objs_normalized[1],[]))
                    output += "  i created a new structure called "+objs[1]+"."
                else: # ok, it exists, but is it a class object?  if not, make it so
                    if self.m.type(self.m.resolve_name(objs_normalized[1]))!='ClassType':
                        self.m.replace_object(self.m.resolve_name(objs_normalized[1]),self.m.new_class_object(self.m.focus+'.'+objs_normalized[1],[]))
                        output += "  i changed "+objs[1]+" into a structure."
                where_to_put = self.m.focus+'.'+objs_normalized[1]
            # is thing singular or plural? 
            if 'determiner=some' in objs_features[0] or 'plural' in objs_features[0]: # plural
                list_full_name = where_to_put+'.'+objs_escaped[0]+'s'
                list_object = self.m.new_list_object(list_full_name,[])
                self.m.add_object(list_object)
                output += "  i created a new list of "+objs[0]+"s within "+self.m.local_name(where_to_put)+"."
            else: # singular
                thing_full_name = where_to_put+'.'+objs_escaped[0]
                thing_object = self.m.new_definition_object(thing_full_name,'None')
                self.m.add_object(thing_object)
                output += "  i created a new thing called "+objs[0]+" within "+self.m.local_name(where_to_put)+".'"

            # the thing/things might have been created within the container... if so, also create class definitions for them
            if (self.m.resolve_name(objs_escaped[0]) not in self.m.dir()):
                thing_full_name = self.m.focus+'.'+objs_escaped[0]
                thing_object = self.m.new_class_object(thing_full_name,[])
                self.m.add_object(thing_object)
                output += "  i created a new thing called "+objs[0]+" within "+self.m.local_name(self.m.focus)+".'"
            else:
                # it already exists, but make sure it is a class
                if self.m.type(self.m.resolve_name(objs_escaped[0])) != 'ClassType':
                    self.m.replace_object(self.m.resolve_name(objs_escaped[0]),self.m.new_class_object(self.m.focus+'.'+objs_escaped[0],[]))
                    output += "  i changed "+objs[0]+" into a structure."
            # is there a subpart specified.. There is a Pacman with a mouth
            if obj_count >= 2 and ('prep=with' in objs_features[1]):
                if not self.m.resolve_name(objs_escaped[0]+'.'+objs_normalized[1]):
                    local_instance_name = 'the_'+objs_normalized[1]
                    new_definition_full_name = self.m.focus+'.'+objs_escaped[0]+'.'+local_instance_name
                    new_definition_object = self.m.new_definition_object(new_definition_full_name,objs_normalized[1]+'()')
                    self.m.add_object(new_definition_object)
                    output += "  i augmented "+objs[0]+" with the part: "+objs[1]+"."
                # also, make a class object on the outside if it doesn't already exist
                if (self.m.resolve_name(objs_normalized[1]) not in self.m.dir()):
                    self.m.add_object(self.m.new_class_object(self.m.focus+'.'+objs_normalized[1],[]))
                    output += "  i created an object called "+objs_normalized[1]+" within "+self.m.local_name(self.m.focus)+'.'
            print("proccess_pp end")    
            return output
        return 'i didn\'t understand that.'
        
                    
        

    def process_response(query):
        if not self.questions_queue or not self.questions_queue[0]['!question_asked'] or not self.questions_queue[0]['!question_requires_answer_p']:
            return
        trimmed_query = query.lower().strip()
        choices = filter(lambda x:x[0]!='!',self.active_question.keys())
        if trimmed_query in choices:
            # perform prescribed actions
            actions_to_perform = self.active_question.get(trimmed_query,[])
            map(lambda x: eval(x), actions_to_perform)
            output = 'ok thanks!'
            # now clear that question from the queue
            del self.questions_queue[0]
            # ask the next question
            if questions_queue:
                questions_queue[0]['!question_asked'] = 1
                output += '  '+questions_queue[0]['!question']
            return output
        else: # response not recognized, give choices
            output = 'i\'m sorry, i didn\'t understand your reply. i was expecting you to say '
            output += string.join(map(lambda x:'"'+x+'"',choices),' or ')
            output += '. please try replying again...'
            return output
        
    def recognize_quotes(self,text):
        # preprocessing of quoted text
        # e.g.: set variable x to "hello world" ===> set variable x to QUOTE_asdDWLLKI
        # where QUOTE_asdDWLLKI is stored in self.lookup under that key
        quote = ''
        escaped_text = ''
        in_quote_p = 0
        text = list(text)
        for i in range(len(text)):
            if text[i] == '"' and not in_quote_p:
                in_quote_p = 1
            elif text[i] == '"' and in_quote_p:
                in_quote_p = 0
                quote_id = 'QUOTE_'+string.join(map(lambda x:random.choice(string.letters),[None]*10),'') # get nonce..cannot be numeric for POS tagger gets tricked by that and marks it as DT
                self.lookup[quote_id] = '"'+quote+'"'
                quote = ''
                escaped_text += ' ' + quote_id + ' '
            elif text[i] != '"' and in_quote_p:
                quote += text[i]
            else:
                escaped_text += text[i]
        return escaped_text

    def recognize_lists(self,text):
        # preprocessing of lists
        # e.g.: the menu includes: beer, some salsa, and chips ===>  menu = LIST_asdDWLLKI
        # where LIST_asdDWLLKI is stored in self.lookup under that key
        the_list = []
        cur_element = ''
        in_list_p = 0
        sentences = self.ml.split_sentences(text)
        for j in range(len(sentences)):
            escaped_text = ''
            text = list(sentences[j])
            for i in range(len(text)):
                if text[i] == ':' and i+1 in range(len(text)) and text[i+1] == ' ' and not in_list_p:
                    in_list_p = 1
                elif text[i] in ['.','!','?'] and in_list_p:
                    the_list.append(cur_element)
                    cur_element = ''
                    in_list_p = 0
                    list_id = 'LIST_'+string.join(map(lambda x:random.choice(string.letters),[None]*10),'') # get nonce..cannot be numeric for POS tagger gets tricked by that and marks it as DT
                    the_list = map(lambda x:' and '.join(self.ml.jist(x)[0]['noun_phrases']),the_list)
                    # strip leading and
                    for i in range(len(the_list)):
                        if the_list[i][:len('and')]=='and':
                            the_list[i]=the_list[i][len('and'):].strip()
                    self.lookup[list_id] = the_list
                    the_list = []
                    escaped_text += ' ' + list_id + ' '
                elif text[i] == ',' and in_list_p:
                    the_list.append(cur_element)
                    cur_element = ''
                elif text[i] != ',' and in_list_p:
                    cur_element += text[i]
                else:
                    escaped_text += text[i]
            sentences[j]=escaped_text.strip('. ')+'. '
        return ' '.join(sentences)
    
    def escape_phrase(self,phrase):
        # takes a phrase and escapes it so that
        # it can be a variable name.
        # currently, changes spaces to _ and omits '
        # deletes leading and_ or or_
        escaped_phrase = phrase.replace(' ','_')
        escaped_phrase = escaped_phrase.replace('\'','')
        if escaped_phrase[:len('and_')]=='and_':
            escaped_phrase = escaped_phrase[len('and_'):]
        if escaped_phrase[:len('or_')]=='or_':
            escaped_phrase = escaped_phrase[len('or_'):]
        print "DEBUGESCAPED",escaped_phrase
        return escaped_phrase

    def normalize_execution_arg(self,raw_arg):
        # decodes any encoded phrase
        arg = self.lookup.get(raw_arg,raw_arg)
        # get rid of prep_ headers
        prep_headers = ['to_','from_','with_','for_','in_','through_','at_','on_','toward_']
        for ph in prep_headers:
            if arg[:len(ph)]==ph:
                arg = arg[len(ph):]
        return arg

    def generalize_phrase(self,phrase):
        # e.g. QUOTE_dsaf ==> quote
        # opportunity for commonsense
        if phrase[:len('QUOTE_')]=='QUOTE_':
            return 'quote'
        return phrase

    def filter_by_tag(self,chunked_text,blacklist,whitelist=None):
        # blacklist looks like: ['DT','MD'] etc
        toks = chunked_text.split()
        for i in range(len(toks)):
            if '/' not in toks[i]:
                continue
            if toks[i].split('/')[1] in blacklist:
                toks[i] = ''
            if whitelist and toks[i].split('/')[1] not in whitelist:
                toks[i]= ''
        toks = filter(lambda x:x!='',toks)
        return ' '.join(toks)

    def strip_tags(self,tagged_or_chunked_text):
    	"""
    	strips part-of-speech and chunk tags from text
    	and returns plaintext
    	"""
        toks = tagged_or_chunked_text.split()
        toks = filter(lambda x:'/' in x,toks)
        toks = map(lambda x:x.split('/')[0],toks)
        return ' '.join(toks)
    
    
    
