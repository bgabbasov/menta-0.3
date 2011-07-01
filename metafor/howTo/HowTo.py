'''
Created on Jun 23, 2011

@author: talanov max
'''
import Report
import string

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

'''
HowTo class name must be in lower case
'''
class install(HowTo):
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

class cleandisk(HowTo):
    
    def __init__(self, parameters=[]):
        self.default_disk = 'C'
        self.disk = self.default_disk
        
        # extract disk name from parameters
        if (len(parameters) > 0 and parameters[0][1:] in string.letters):
            self.disk = parameters[0][1:]
        
    def apply(self):
        r = "cleaning disk " + str(self.disk)
        return Report.Report(r)

class ask_(HowTo):
    
    def apply(self):
        return Report.Report("What does that mean ?")                