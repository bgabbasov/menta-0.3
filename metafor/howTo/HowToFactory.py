'''
Created on 24.06.2011

@author: talanov max
'''
from howTo.HowTo import Install, CleanDisk

class HowToFactory(object):
    '''
    It is the factory to crate HowTo-s.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def createHowTo(self, howToId):
        if howToId == 'Install':
            return Install()
        elif howToId == 'CleanDisk':
            return CleanDisk()