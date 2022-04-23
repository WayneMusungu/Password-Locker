import unittest #  We import the unittest module
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("Wayne","Musungu","yyy@gmail.com","ORTIZ","12345") #Create user object
        
    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        
        self.assertEqual(self.new_user.first_name,"Wayne")
        self.assertEqual(self.new_user.last_name,"Musungu")
        self.assertEqual(self.new_user.email,"yyy@gmail.com")
        self.assertEqual(self.new_user.username,"ORTIZ")
        self.assertEqual(self.new_user.password,"12345")
        
        
if __name__ == '__main__':
    unittest.main()
    
    