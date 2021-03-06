import pyperclip
import string
from random import choice

class User: 
    '''
    We create a class that generates new instances of users
    '''
    pass

    user_list = [] #Empty user list
    
    def __init__(self,first_name,last_name,email,username,password):
        
        '''
        The __init__ method helps us define proprties of our objects 
        
        Args:
        first_name: New user firstname.
        last_name: New user last name.
        email: New user email address.
        username: New user username.
        password: New user password.
        
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
      
    
    def save_user(self):
        
        '''
        save_user method saves contact objects into user_list
        '''
        
        User.user_list.append(self)
        
    
    @classmethod
    def authenticate_user(cls,username,password):
        '''
        Method to authenticate the user 
        '''
        verify_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                verify_user == user.name
            return verify_user
        

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        
        User.user_list.remove(self)
        
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in username and returns a user that matches the username
        
        Args:
            username: User's name to search for
            
        Returns:
            User that matches the username
        '''
        
        for user in cls.user_list:
            if user.username == username:
                return user
                
    
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if the username exists from the user list.
        
        Args:
            username: Username to search if it exists
        Returns:
            Boolean: True or false depending if the username exists
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        
        return cls.user_list
    
    def generate_random_password(length = 10 ):
        '''
        Method that generates a random alphanumeric and special characters
        '''
        
        password = string.digits + string.ascii_lowercase + string.ascii_uppercase + "~!@#$%^&*`"
        
        return ''.join(choice(password) for i in range(length))
    
    @classmethod
    def copy_email(cls,username):
        user_found = User.find_by_username(username)
        pyperclip.copy(user_found.email)
    
        
   