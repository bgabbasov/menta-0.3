'''
Created on 14.07.2011

@author: talanov max
'''
import logging
import unittest
import Metafor

__author__ = 'talanovm'


class TestRegression(unittest.TestCase):

    def setUp(self):
        self.theMetafor = Metafor.Metafor()
        self.log = logging.getLogger("TestRegression")

    def apply(self, query):
        self.theMetafor.nl.clear_model()
        self.theMetafor.objects =  [['__main__', 'FunctionType', [], []]]
        response = self.theMetafor.handle_query(query)
        self.log.debug("response \n %s", response)

        python_code = self.theMetafor.render_code(full_name='__main__', flavor='python')
        self.log.debug("STRUCTURE: \n%s", python_code)
        res=self.theMetafor.render_code(full_name='__main__', flavor='howTo')
        self.log.debug("HowTo: \n%s", res)
        return res
# Account operations test
    def test_account_operations_1(self):
        query = "I have forgotten password and have blocked an account."
        assertion = "     I reset your password !\n     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_account_operations_2(self):
        query = "I have blocked an account."
        assertion = "     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_account_operations_3(self):
        query = "Please reset password."
        assertion = "     I reset your password !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_account_operations_4(self):
        query = "Please unblock my account."
        assertion = "     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

# Clean disk tests:
    def test_clean_disk_operations_1(self):
        query = "Laptop - user has almost full C:\\"
        assertion = "     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_clean_disk_operations_2(self):
        query = "Please clean disk C:"
        assertion = "     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_clean_disk_operations_3(self):
        query = "There is insufficient disk space on C:"
        assertion = "     I reset your account to unlocked state !\n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

# Install tests
    def test_install_software_operations_1(self):
        query = "Install Firefox."
        assertion = "     installing application: Firefox...\n     \n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

    def test_install_software_operations_2(self):
        query = "Please install Chrome."
        assertion = "     installing application: Chrome...\n     \n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

# Invalid HowTo test
    def test_inavalid_howTo_operations_2(self):
        query = "terminate now"
        assertion = "     Can't terminate\n     \n     "
        temp = self.apply(query)
        self.assertEqual(temp, assertion)

if __name__ == '__main__':
    unittest.main()
  