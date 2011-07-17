'''
Created on Jun 23, 2011

@author: talanov max
'''
import Report
import string
import logging
import os
import subprocess

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
&
applicationsToInstall must be in lower case
'''
class install(HowTo):
    applicationsToInstall = ['firefox', 'chrome', 'google_chrome', 'microsoft_word', 'word', 'microsoft_office', 'ms_office']
    install_cmd_ending = ".bat"
    install_cmd_prefix = "install_scripts"
    cmd_delimiter = "\\"
    
    def __init__(self, parameters=[]):
        inListApplications = []
        if (len(parameters) < 1):
            logging.error("Parameters of install HowTo are not specified.")
            raise ValueError("Please specify application to install.")
        for par in parameters:
            if (par.lower() in self.applicationsToInstall):
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
            ending = self.install_cmd_ending
            delimiter = self.cmd_delimiter
            if (("nt" in os.name) or ("windows" in os.name) ):
                delimiter = "\\" 
                ending = ".bat"
            else:
                delimiter = "/"
                ending = ".sh"
            cmd = self.install_cmd_prefix + delimiter + a + ending
            logging.debug(cmd)
            try:
                retcode = subprocess.call([cmd])
            except ValueError, e:
                retcode = str(e)
            except OSError, e: 
                retcode = str(e)
            logging.debug(retcode)     
        return Report.Report(r)

class cleandisk(HowTo):
    
    def __init__(self, parameters=[]):
        self.default_disk = 'Z'
        self.disk = self.default_disk
        
        # extract disk name from parameters
        if (len(parameters) > 0 and parameters[0][len(parameters[0])-1] in string.letters):
            self.disk = parameters[0][len(parameters[0])-1]
        else:
            self.disk = None
        
    def apply(self):
        r = ""
        if (self.disk == None):
            r = "Please specify disk"
        else:
            r = "cleaning disk " + str(self.disk)
        return Report.Report(r)

class ask_(HowTo):
    
    def apply(self):
        return Report.Report("What does it mean?")                