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
    
    def __init__(self, applicationName, filepath):
        self.applicationName = applicationName
        self.filepath = filepath
        
    def apply(self):
        reportContents = "installing application: " + self.applicationName
        return Report.Report(reportContents)
                