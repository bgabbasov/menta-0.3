'''
Created on 24.06.2011
Class to crate HowTo-s.
@author: talanov max
'''
import logging
import howTo
from howTo.HowTo import ErrorHowTo
from howTo.Report import Report

class HowToFactory(object):
    '''
    It is the factory to crate HowTo-s.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.prefix = u'__main__.Menta.'
    
    def createHowTo(self, howToId, parameters):
        
        account_operations = ['i.block', 'block',  'unblock', '__main__.i.block']
        password_operations = ['i.forget', 'reset', '__main__.i.forget']
        clean_disk_operation = "clean_disk"
        insufficient_disk_suffix = "c.insufficient_disk_space"
        insufficient_disk_prefix = "__main__."

#        class Menta:
#          def Please(clean_disk_C):
        
        # use introspection to create HowTo
        HowToFuncName=howToId.replace(self.prefix, "").lower()
        
        
        if HowToFuncName in account_operations and parameters[0]=='account':
            HowToFuncName='unblock'
        elif HowToFuncName in password_operations and parameters[0]=='password':
            HowToFuncName='resetpassword'
        elif HowToFuncName == 'please' and parameters[0]=='reset_password':
            HowToFuncName='resetpassword'
        elif HowToFuncName == 'please' and parameters[0].startswith(clean_disk_operation):
            HowToFuncName = "clean_disk"
        elif HowToFuncName.endswith(insufficient_disk_suffix):
            HowToFuncName = "clean_disk"
            temp_parameters = []
            for i in parameters:
                if (i != None and i.startswith(insufficient_disk_prefix)):
                    temp_parameters.append(i.replace(insufficient_disk_prefix,""))
                    logging.debug("temp_parameters: %s", str(temp_parameters))
            parameters = temp_parameters
        
        try:
            ht = getattr(howTo.HowTo, HowToFuncName)
        except Exception:
            ht = getattr(howTo.HowTo, 'ask_')
        try:
            parameters.insert(0,HowToFuncName)
            logging.debug(ht)
            logging.debug(parameters)
            iht = ht(parameters)

            return iht
        except ValueError, e:
            logging.error(str(e))
            r = Report(str(e))
            e = ErrorHowTo(r)   
            return e
            
        