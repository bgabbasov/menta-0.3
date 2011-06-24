'''
Created on Jun 23, 2011

@author: talanov max
'''
import Report

class HowTo(object):
    '''
    Main class of howTo-s.
    '''

    def __init__(self, selfparams):
        '''
        Constructor
        '''
        
    def apply(self):
        return Report.Report()


class Install(HowTo):
    
    def __init__(self, applicationName='Firefox', filepath='./'):
        self.applicationName = applicationName
        self.filepath = filepath
        
    def apply(self):
        r = "installing application: " + self.applicationName
        return Report.Report(r)

class CleanDisk(HowTo):
    
    def __init__(self, diskPath = './'):
        self.disk = diskPath
    
    def apply(self):
        r = "cleaning disk " + self.disk
        return Report.Report(r)                