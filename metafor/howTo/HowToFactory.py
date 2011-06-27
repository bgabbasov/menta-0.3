'''
Created on 24.06.2011

@author: talanov max
'''
from howTo.HowTo import install, cleandisk
import howTo

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
        return ht(parameters)
        
        
#        if howToId == self.prefix + 'Install':
#            return Install(parameters)
#        elif howToId == self.prefix + 'CleanDisk':
#            return CleanDisk()