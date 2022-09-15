# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:02:34 2022

@author: mingt
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'First flask app!'

app.run(port = 4999)

# ----
# GET Request is a 'verb'
# GET  /     HTTP/1.1
# Verb path  protocol
# ----

# server will respond accordingly i.e.
# ----
# Error if path '/' is not found 
# Error if http is not supported i.e. mail suerver only support smtp, or it's an fdp server
# Error if server is currently unavailable 
# html code back (in google case)
# text 
# nothing if server not configured 
# ----

# Going to any page using browser is a get request 
# -----
# https://twitter.com/login	GET / login HTTP1.1 Host: https//twitter.com
# This perform get request "get/login"
# "https://twitter.com" is the host name 
# "/login" is the path
# -----
# https://git-scm.com/download/mac
# "https://git-scm.com"  host name 
# "/download/mac" is the path
# -----
# https://www.google.ca/
# "https://www.google.ca" host name
# "/" is the path, which is the root

# these servers responds GET requests (when someone visiting a page) with their own html code
# (loging page, download for mac page, home page)	  
# Browser is configured to do a get request

# Other actions such as POST, DELETE, PUT, OPTIONS, HEAD etc 	 

# GET: Retrieve something, GET /item/1 In the case of API, retreive an item with id "1"
# POST: receive data and use it,    POST /item  (i.e. josn item {'name': 'Chair', 'price': 9.99}
#  	 (Also when doing post request some data ( a piece of json) will be sent along the request)
# PUT: make sure something is there, PUT /item (it make create previous json if not existed, or update it)
# DEL: remove something, DELETE /item/1


