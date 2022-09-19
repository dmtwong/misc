# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:45:59 2022

@author: mingt
"""

 # On top of '_oneRes' add items resource to print out all the items
 
from flask import Flask #, request
from flask_restful import Resource, Api#, reqparse


app = Flask(__name__)
api = Api(app)

items = [] # again for simiplicity use in memeory data: items as as list

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
            else:
                return  {'item': None}, 404
            
    def post(self, name): 
        # pass
        item = {'name': name,
                'price': -99.99
            }
        items.append(item)
        return item, 201 # 201 is for created status
        # 202 is for accepted (when creation is delayed, it may still fail though)

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200
        

api.add_resource(Item, '/item/<string:name>') # replace decorator aboved
api.add_resource(ItemList, '/items') # replace decorator aboved

app.run(port = 5000, debug = True) # an html page for debug