# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:30:12 2022

@author: mingt
"""
# simulate an online store

# Write as a server but remember from browser perspective, 
# POST request send data, and GET to get data
 
from flask import Flask

app = Flask(__name__)

# For pratical case it should be a database; here is using dict in memory as example
# store is a list that has each store as a dict
# each store itself has two keys: store with string and item with a list
# the items key in each store is associated with a list of items
# each item is rep by a dict that gives name and price 
stores =  [
    {'name': 'Store A',
     'items': [
         {
             'name': 'Store A item A apple',
             'price': 0.99
             }
         ]
    }
    ]

# We will get the name of store to create (POST) 
# and send the name list back (GET) 

# POST /store dataL {name:}
@app.route('/store', methods = ['POST']) # by default is a GET request, the endpoint can be accesiable bia GET and POST in the sametime
def create_a_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def print_a_store_name(name): # parameter match above; cosnider /store/name_A, then the name will be matched to 'name_A'
    pass

# GET /store
@app.route('/store')
def print_store_list(): 
    pass 

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_from_a_store(name):
    pass

# GET /store//<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_from_a_store(name):
    pass

# def home():
#   return 'First flask app!'
 
# app.run(port = 4999)

############

# What is a REST API
# A way to think how a web serve responds to your requests
# - not just respond with data but with resources (still data but it's the concept; asking for a resource in the server)
# - similar to oop (server as having resources, and they interact with the pertinent request)


# Consider a server has an endpoint 'item' resource for all 4 above actions
# GET, POST, PUT, DELETE path /item/chair and POST PUT with some extra data (i.e. price change )
# They have same endpoint and accessing the same 'item' resource ('chair' element of the 'item' resource)
# - We should think of the interactions with server as resources insteads of individual request 
# - instead of dealing with endpoints, we are dealing with resources (cosnide 'item' as object)
# also an endpoint 'items' resource


# -----------------
# Stateless: one request should not depend on any other request; 
# server only need to knows the current requests not previous requests
# - POST /item/chair is requested
# - server does not know it is now existed even in database 
# - GET /item/chair goes to database and has to check whether 'chair' element exists and return 

# 	
# Consider logging into a web application like twitter
# server respond with some data that are unique to the user (authentication) 
# - The web server does not know user is logged in  
# - Web application must send enough data to identify in every request when interacts with server
# so that the server know the user is indeed logged in [the piece of unique data the serve returned when we logged in] 
# or server will not be able to accociate with user 

