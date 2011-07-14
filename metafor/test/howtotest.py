'''
Created on 14.07.2011

@author: talanov m
'''
import unittest
import subprocess
import logging

class TestHowTo(unittest.TestCase):
    
    def setUp(self):
        pass

#    def testshuffle(self):
#        # make sure the shuffled sequence does not lose any elements
#        random.shuffle(self.seq)
#        self.seq.sort()
#        self.assertEqual(self.seq, range(10))
#
#    def testchoice(self):
#        element = random.choice(self.seq)
#        self.assert_(element in self.seq)
#
#    def testsample(self):
#        self.assertRaises(ValueError, random.sample, self.seq, 20)
#        for element in random.sample(self.seq, 5):
#            self.assert_(element in self.seq)


    def test_command_call(self):
        retcode = subprocess.call(["ls", "-l"])
        logging.debug(retcode)
        
    def test_bat_call(self):
        retcode = subprocess.call(["test.bat"])
        logging.debug(retcode)

if __name__ == '__main__':
    unittest.main()