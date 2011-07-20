'''
Created on Jun 23, 2011

@author: talanov max
'''
class Report(object):
    
    contents = ""
    
    def __init__(self, aContents):
        self.contents = aContents
        
    def getContents(self):
        return self.contents
    
    def setContents(self, aContents):
        self.contents = aContents