# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:45:59 2022

@author: mingt
"""
# Update two requests from item resource 
 # 1. mod GET method; replace the ugly for loop, this approach 
 # can help establish rep invar and prevent bad req (no dup item) with changes in POST request
 # 2. mod POST method of Item resource as 1 noted; also read to take json payload into the picture
 
from flask import Flask, request
from flask_restful import Resource, Api#, reqparse


app = Flask(__name__)
api = Api(app)

items = [] 

class Item(Resource):
    def get(self, name):
        # filter object can be used with next; will return error if not found in it
        item = next(filter(lambda x: x['name'] == name, items), None) 
        return  {'item': item}, 200 if item is not None else 404 # is not None given to make it explicit only
            
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None): # iter
            return {'message': "name '{}' is already existed".format(name)}, 400 # bad request status       
        data = request.get_json() # dict type; error if request doesnot attach with json/inproper content-type header
        # data = request.get_json(force = True) # alt 1: header dismatch become irrelevant which maybe misleading 
        # data = request.get_json(silent= True) # alt 2: return none if error
        item = {'name': name,
                'price': data['price']
            }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200
        

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items') 

app.run(port = 5000)