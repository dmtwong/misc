# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:02:34 2022

@author: mingt
"""


# decorator usage illustration 
# Example 1:
user = {"username:": "jose", "access_level": "guest"}
user
def get_admin_password():
    return "1234"

print(get_admin_password())

# if user["access_level"] == "admin":
#     print(get_admin_password())

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

print(secure_get_admin())

##  
def secure_function(func):
     if user["access_level"] == "admin":
         return func

get_admin_password = secure_function(get_admin_password)
get_admin_password()
user = {"username:": "jose", 
        "access_level": "admin"}
def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"
get_admin_password = secure_function(get_admin_password)
get_admin_password()

## get_admin_password() get pass to make_secure() return function
## instead of function call
user = {"username": "jose", "access_level": "guest"}

import functools
def make_secure(func):
    @functools.wraps(func) # tell the wrapper function below that it is a wrapper for'func'
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No permissions for {user['username']}"
    return secure_function

@make_secure

def get_admin_password():
    return "1234"
get_admin_password = make_secure(get_admin_password)
get_admin_password()
user = {"username": "jose", "access_level": "admin"}
get_admin_password()
print(get_admin_password())
print(get_admin_password.__name__)

################## with parameter
import functools
user = {"username": "jose", "access_level": "guest"}
def make_secure(func):
    @functools.wraps(func) # tell the wrapper function below that it is a wrapper for'func'
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No permissions for {user['username']}"
    return secure_function
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
get_password("billing")
get_password("admin")
get_password()


################## with parameter

import functools
user = {"username": "jose", "access_level": "guest"}
def make_secure(func):
    @functools.wraps(func) # tell the wrapper function below that it is a wrapper for'func'
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No permissions for {user['username']}"
    return secure_function

# when below gets called make_secure get applied to get_admin_password 
@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

get_password("billing")
get_password("admin")
# print(get_password("billing"))
get_password()

################## with parameter
inst