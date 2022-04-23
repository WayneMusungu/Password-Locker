import unittest # Importing the unittest module
from credentials import Credentials #Importing the credential class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    
    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Facebook","Ning","8863")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"Facebook")
        self.assertEqual(self.new_credential.username,"Ning")
        self.assertEqual(self.new_credential.password,"8863")
        
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved in to
        the credential list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        tearDown method that does cean up after each test case has run. 
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our credential_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Snapchat","Whitney","blindislove")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    
        
if __name__ == '__main__':
    unittest.main()