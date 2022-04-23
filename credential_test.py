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
        
if __name__ == '__main__':
    unittest.main()