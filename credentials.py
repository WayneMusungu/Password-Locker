class Credentials:
    '''
    We create a class that generates new instances of credentials
    '''
    pass


    credentials_list = []
    
    def __init__(self,account,username,password):
        '''
        The __init__ method helps us define proprties of our objects 
        
        Args:
        account: New credential account.
        username: New credential username.
        password: New credential password.
        '''
        
        self.account = account
        self.username = username
        self.password = password


