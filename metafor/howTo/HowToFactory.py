'''
Created on 24.06.2011

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
        # use introspection to create HowTo
        try:
            ht = getattr(howTo.HowTo, howToId.replace(self.prefix, "").lower())
        except Exception:
            ht = getattr(howTo.HowTo, 'ask_')
        try:
            return ht(parameters)
        except ValueError as e:
            logging.error(str(e))
            r = Report(str(e))
            e = ErrorHowTo(r)   
            return e
            
        