'''
Created on Jun 23, 2011

@author: talanov max
'''
import Report
import string
import logging

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

class ErrorHowTo(HowTo):
    
    def __init__(self, parameter):
        if (parameter != None):
            self.report = parameter
        else:
            self.report = Report.Report("Empty Error report")
            
    def apply(self):
        return self.report 

'''
HowTo class name must be in lower case
'''
class install(HowTo):
    applicationsToInstall = ['Firefox', 'firefox', 'Chrome', "chrome", 'Google_Chrome', "google_chrome", 'Microsoft_Word', 'Word', "word"]
    
    def __init__(self, parameters=[]):
        inListApplications = []
        if (len(parameters) < 1):
            logging.error("Parameters of install HowTo are not specified.")
            raise ValueError("Please specify application to install.")
        for par in parameters:
            if (par in self.applicationsToInstall):
                inListApplications.append(par)
        if(len(inListApplications) < 1):
            logging.error("Application is not in list")
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
        self.default_disk = 'Z'
        self.disk = self.default_disk
        
        # extract disk name from parameters
        if (len(parameters) > 0 and parameters[0][len(parameters[0])-1] in string.letters):
            self.disk = parameters[0][len(parameters[0])-1]
        
    def apply(self):
        r = "cleaning disk " + str(self.disk)
        return Report.Report(r)

class ask_(HowTo):
    
    def apply(self):
        return Report.Report("Error: What does it mean?")                