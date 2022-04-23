from cgi import test
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
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the contact list
        '''
        
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)
     
     
     
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        User.user_list = []
        
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple contact objects to the user_list
        '''
        
        self.new_user.save_user()
        test_user = User("Pablo","Zabaleta","zaba@qq.com","Pablo","09876") #New contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        
        self.new_user.save_user()
        test_user = User("Pablo","Zabaleta","zaba@qq.com","Pablo","09876")#New contact
        test_user.save_user() 
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
        
        
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display information
        '''
        
        self.new_user.save_user()
        test_user = User("Pablo","Zabaleta","zaba@qq.com","Pablo","09876")#New contact
        test_user.save_user()
        found_user = User.find_by_username("Pablo")
        self.assertEqual(found_user.username, test_user.username)
        
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the username
        '''
        
        self.new_user.save_user()
        test_user = User("Pablo","Zabaleta","zaba@qq.com","Pablo","09876")#New contact
        test_user.save_user()
        
        user_exits = User.user_exist("Pablo")
        self.assertTrue(user_exits)
        
   
if __name__ == '__main__':
    unittest.main()
    
    