#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

# Create user function
def create_user(fname,lname,uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,uname,password)
    return new_user

def save_users(user):
    '''
    Function to dave a user
    '''
    user.save_user()  
    
def login_user(username,password):
    '''
    Function that allows an existing user to login
    '''
    new_entry = User.authenticate_user(username,password)
    return new_entry


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
def create_credential(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credential(credentials):
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
    
