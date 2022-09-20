# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:06:38 2022

@author: mingt
"""

# import os
# print(os.getcwd())

class User:
    '''Store User data'''
    # Each user instance has the same attribute as the key of elements in
    # user list inside security 101
    def __init__(self, _id, name, pwd): # underscore added as id itself is a python keyword
        self.id = _id 
        self.username = name
        self.password = pwd
    
    def __str__(self):
        # print('User id: ' + self.id + 'has username: ' +self.username)
        return 'User id: ' + self.id + 'has username: ' +self.username