# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:06:54 2022

@author: mingt
"""
# Including only two endpoints of ITEM resource for the store api 
# (ignore put and del as well as ITEMS resource)
# Note 2: with flask_restful no need to import jsonify
 
from flask import Flask #, request
from flask_restful import Resource, Api#, reqparse


app = Flask(__name__)
api = Api(app)

items = [] # again for simiplicity use in memeory data: items as as list

class Item(Resource):
    # # @app.route('/item/<string:name>') no longer needed wtih Api method
    # get will look at the list (database) and match the requested <name>
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
            else:
                return  {'item': None}, 404# without else clause it will return null and 
            # json have to be dict form (invalid json, ok for postman but not like angular JS)
            # 404 is added or else postman will show 200 OK for status
        
        # return {'item': name}
    
    # post need to have the exact same signiture/parameters
    # as /item/<string:name>' will dispatch for 'name' parameters
    # even though this request has a json payload (data can be sent via json)
    # so tech we can send the name via json but dont do that
    # simply receive it via url as these things should be accessed
    # at the same endpoint by changing the http verb
    # NOTE: baby step give a rep init val -99.99 
    # without looking at the json, and it will be changed later
    # NOTE2: tell client (POSTMAN in the example, could be a mobile/web app)
    # that we create this item and added to items (database in reality)
    def post(self, name): 
        # pass
        item = {'name': name,
                'price': -99.99
            }
        items.append(item)
        return item, 201 # it is added to let the app know it happened instead of none
        # 201 is for created status
        # 202 is for accepted (when creation is delayed, it may still fail though)
api.add_resource(Item, '/item/<string:name>') # replace decorator aboved

app.run(port = 5000)