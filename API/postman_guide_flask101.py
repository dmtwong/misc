# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:26:05 2022

@author: mingt
"""

# Test first design of API help design/develope api more efficiently
# put all the related request for one apo in a sep folder of postman
# Think what requests the api needed will help a lot when writing api
# just like planning test cases when writing normal program
# It force us to think how the API should be designed during the process
# i.e. how resource should be 'seperated'/encap
# once it's designed, we simply need to use this structure 
# to write resources on python code (for store example 2 resources so far)

# start making endpoints without realizing whether they are necessary
# is not a good habit

# Consider the store item example we have two rest resource

# R1: /items will simply return an item list (1 request only)
# this api we need to 1) get all of the items that are available (/item)
# on postman put down http://127.0.0.1:5000/items on request URL
# and Save it with spec we expect return before writing code


# The next four requests will belong to same resource (/item<name>)
# 2) access specific item (create another request)
# say /item/apple or /item/1234 depending whether you design 
# individual item have unique name or id instead 
# i.e. if situation expect dup item name we cannot access like /item/Mac for two different item
# /item/<name>

# 3. not just the GET method for  /item/<name> but algo POST method
# for 'Headers' choose key: Content-Type and value: application/json
# for 'body' choose raw and json(app/json) and select info that 
# the api is going to receive when post request is made (what data to be stored for an item)
# {
#  "price" : -99.99
#  }
# make it specificy in desc that it will fail if same <name> was already existed


# 4. beside GET and POST method, DELETE is needed for /item/<name>
# only need the unique reference what is <name>
# no headers nor body is needed

# 5. PUT is also needed indeed; for modify the individual item
# RECALL:POST send data to server and gather with the data and create new stuff
# PUT give data to server and do one of two things:
    # 1.) create a new item
    # or 2.) update and existing item that already exist with that unique <name>
# It will have same headers 
# and change it in body, in this case another value for price
# Do it 10 times it wont fail but only first time may make a difference


    





from flask import Flask #, request
from flask_restful import Resource, Api#, reqparse


app = Flask(__name__)

api = Api(app)

class Item(Resource):
    # @app.route('/item/<string:name>') no longer needed wtih Api method
    def get(self, name):
        return {'item': name}

api.add_resource(Item, '/item/<string:name>') # replace decorator aboved

app.run(port = 5000)