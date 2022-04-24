#!/usr/bin/env python3.8

from user import User
from credentials import Credentials


def create_user(fname,lname,uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,uname,password)
    return new_user

def login_user(username,password):
    '''
    Function that allows an existing user to login
    '''
    new_entry = User.verify_user(username,password)
    return new_entry