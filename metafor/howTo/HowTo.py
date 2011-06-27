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
    applicationsToInstall = ['Firefox', 'firefox', 'Chrome', 'Google Chrome', 'Microsoft Word', 'Word']
    
    def __init__(self, parameters=[]):
        inListApplications = []
        for par in parameters:
            if (par in self.applicationsToInstall):
                inListApplications.append(par)
        if(len(inListApplications) < 0):
            raise ValueError("Application is not in supported list")
        else:
            self.applicationName = inListApplications
            
    def apply(self):
        r = ""
        for a in self.applicationName: 
            r += "installing application: " + a + "...\n"
        return Report.Report(r)

class CleanDisk(HowTo):
    
    def __init__(self, diskPath = './'):
        self.disk = diskPath
    
    def apply(self):
        r = "cleaning disk " + self.disk
        return Report.Report(r)                