# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:57:08 2022

@author: mingt
"""

from user import User 
# Self note: find something to replace as hmac no longer usable synatx stayed at python 2 
# from hmac import safe_str_cmp

# This contains
# 1. a table/list of registered users (user instance in memory now and show be database)
# 2. a dict using name and id as key for mapping respectively (or else need to loop over above list?)
# 3. Function to autherticate users (directly retreive user id or name without looping over list)
# User class inside user.py within same folder
# writing each user as an instance of User is better for data abs

users = [
    # {
    # 'id': 1,
    # 'username': 'htc',
    # 'password': 'iphone4'    
    # }, 
    User(1, 'htc', 'iphone4'), User(2, 'blackberry', 'uncleSamsung')
    # {
    # 'id': 2,
    # 'username': 'blackberry',
    # 'password': 'uncleSamsung'    
    # }
        ]
        
name_mapping = { 
    # 'htc': {
    #     'id' : 1,
    #     'username': 'htc',
    #     'password': 'iphone4'  
    #     },
    # 'blackberry': {
    #     'id': 2,
    #     'username': 'blackberry',
    #     'password': 'uncleSamsung'  
    #     }
    use.username: use for use in users 
    }


# print(type(name_mapping), name_mapping)
# class 'dict'> {'htc': <user.User object at 0x00000202B79B4CD0>}

# print(name_mapping)

id_mapping = {
    # 1: {    
    #     'id': 1,
    #     'username': 'htc',
    #     'password': 'iphone4'    
    # },
    # 2: {
    #     'id': 2,
    #     'username': 'blackberry',
    #     'password': 'uncleSamsung'        
    #     }
    use.id: use for use in users
    }
# print(id_mapping)

def authenticate(username, password):
    # Input: valid user name and password
    # Output: select correct user name from the list or return None silently 
    user = name_mapping.get(username, None) # get method of dict allow default value if not found nth spec other than that
    if user != None and user.password == password: # safe_str_cmp(user.password, password): # user['password'] == password:
        return user

def identity(payload):
    # Input: contents of JWT Token
    # Output: retreive specific user that match the input or else None
    user_id = payload['id'] # Extract the userid from input
    return id_mapping.get(user_id, None)


