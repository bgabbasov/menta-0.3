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
        
        try:
            ht = getattr(howTo.HowTo, HowToFuncName)
        except Exception:
            ht = getattr(howTo.HowTo, 'ask_')
        try:
            return ht(parameters)
        except ValueError, e:
            logging.error(str(e))
            r = Report(str(e))
            e = ErrorHowTo(r)   
            return e
            
        