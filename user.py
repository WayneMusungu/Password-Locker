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
                
        
   