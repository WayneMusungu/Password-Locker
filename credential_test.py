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
        test_credential = Credentials("Snapchat","Whitney","blindislove")#New credential
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
        
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove credentials from our
        credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Snapchat","Whitney","blindislove")#New credential
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
        
    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential entry by account name and display
        the details of the credential
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Snapchat","Whitney","blindislove")#New credential
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account("Snapchat")

        self.assertEqual(found_credential.account,test_credential.account)
        
        
    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean if we cannot find the credential.
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Snapchat","Whitney","blindislove")#New credential
        test_credential.save_credentials()

        credential_exists = Credentials.credential_exist("Snapchat")

        self.assertTrue(credential_exists)
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        


    
        
if __name__ == '__main__':
    unittest.main()