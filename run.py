#!/usr/bin/env python3.8

from user import User
from credentials import Credentials


# Create user function
def create_user(fname,lname,email,uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,uname,password)
    return new_user

def login_user(username,password):
    '''
    Function that allows an existing user to login
    '''
    new_entry = User.authenticate_user(username,password)
    return new_entry

def save_users(user):
    '''
    Function to dave a user
    '''
    user.save_user()  
    

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(username):
    '''
    Function that find a user by their username and returns the user
    '''
    return User.find_by_username(username)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# Create credential functions
def create_credentials(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
    
def delete_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(account):
    '''
    Function that finds a Credentials account name and returns the credential
    '''
    return Credentials.find_by_account(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def generate_password():
    '''
    Generates a random password for the user
    '''
    
    new_password = Credentials.generate_random_password()
    
    return new_password

def main():
    print("Hey you there 😹!!! Welcome to Password-locker an application that stores your account credentials\n Kindly enter the following short codes to proceed 😉\n (1) CNA ---- Create New Account\n (2) HAA ---- Have An Account\n")
    

    short_code = input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('_' * 60)
        
        fname = input("First name: ")
        lname = input("Last name: ")
        email = input("Email: ")
        uname = input("Username: ")
        while True:
            print("TYP -- To type your own password")
            print("GRP -- To generate random password")
            password_Choice = input().lower().strip()
            if password_Choice == 'typ':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'grp':
                password = generate_password()
                break
            

            else:
                print("Invalid entry kindly key in the initials TYP or GRP to proceed")
            
        save_users(create_user(fname,lname,email,uname,password))
        print("_" * 50)
        print(f"Congratulations {fname} {lname} on setting up your account🍾🥂! Please keep a note of your login account details:\n USERNAME: {uname}\n EMAIL: {email}\n PASSWORD: {password}")
        print("_" * 60)
        
        
    elif short_code == "haa":
        print("_" * 60)
    
        print("Seems you are back 😃 😃. Enter your Username and Password to login:")
       
        print('_' * 60)
        uname = input("Username: ")
        password = input("password: ")
        login_user(uname,password)
        print('\n')
        print(f"Hello {uname}!! Welcome to the Password locker APP 😍😍")
        print('\n')
       
        while True:
            print("Use these short codes:\n (1) CNC ----  Create New Credentials\n (2) DC ---- Display Credentials\n (3) FC ----Find Credentials\n (4) GRP ---- Generate Random Password\n (5) DEL ---- Delete Credential\n (6) EX ----Exit the application\n")
            short_code = input().lower().strip()
            if short_code == "cnc":
                print("Create New Credential")
                print("_"*20)
                print("Account name:")
                account = input().capitalize()
                print("Your Account username:")
                username = input()
                while True:
                    print("TYP - To type your password on your already existing account:\nGRP- To be generated for Password")
                    password_Choice = input().lower().strip()
                    if password_Choice == 'typ':
                        password = input("Enter Your password\n")
                        break
                    elif password_Choice == 'grp':
                        password = generate_password()
                        break
                    else:
                        print("Invalid entry kindly key in the initials TYP or GRP to proceed ❗️")

                save_credentials(create_credentials(account,username,password))
                print('\n')
                print(f"Account Credentials for {account} - Username: {username} & Password: {password}, was created successfully 💯💯") 
                print('\n')

            elif short_code == "dc":
                if display_credentials():
                    print("Here's your list of account(s): ")

                    print('_' * 30)
                    print('_'*30)

                    for account in display_credentials():
                        print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                        print('_' * 30)
                        print('_' * 30)
                else:
                    print("Whoopsie!!! It seems you don't have any credentials saved yet 💔")

            elif short_code == "fc":
                print("Enter the Account Name you want to search for")
                search_name = input().lower()
                if find_credentials(search_name):
                    search_credential = find_credentials(search_name)
                    print(f"Account Name: {search_credential.account}")
                    print('-' * 50)
                    print(f"Username: {search_credential.username} Password :{search_credential.password}")
                    print('-' * 50)
                else:
                    print("The Credential does not exist🤦‍♂🤡 ")
                    print('\n')
            elif short_code == "del":
                print("Enter the Account Name Credentials that you want to delete")
                search_name = input().lower()
                if find_credentials(search_name):
                    search_credential = find_credentials(search_name)
                    print("_" * 50)
                    search_credential.delete_credentials()
                    print('\n')
                    print(f"New Credential:{search_credential.credential}Your stored credentials for : {search_credential.account} successfully deleted")
                    print('\n')
                else:
                    print("The Credential does not exist")
            
            elif short_code == 'grp':
                password = generate_password()
                print(f" {password} Has been generated successfully.")
            
            elif short_code == 'ex':
                print("_"*50)
                print("Warning! You will loose all your credentials if you exit the application. Are you sure? y/n")
                logout = input().lower()
                print("_"*50)
                if logout == 'y':
                        print("Thank you for using Password-locker. See you next time buddy 👋👋👋!!")
                        break
                elif logout == 'n':
                        continue
            else:
                print("Couldn't recognize that.Kindly input a valid short code")
            
    else:
        print("Please enter a valid short code to proceed ❗️❗️❗️")
        
        
            
            
            
            
            
            
            
            
            
    
                
        

            
            
            
        
    


if __name__ == '__main__':
    main()