'''
Created on 24.06.2011

@author: talanov max
'''
from howTo.HowTo import Install, CleanDisk
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
        ht = getattr(howTo.HowTo, howToId.replace(self.prefix, ""))
        return ht(parameters)
        
        
#        if howToId == self.prefix + 'Install':
#            return Install(parameters)
#        elif howToId == self.prefix + 'CleanDisk':
#            return CleanDisk()