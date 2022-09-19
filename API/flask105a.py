# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:24:28 2022

@author: mingt
"""
# making an api, defining method for the resource 
# (in this case only get method for Item resource)
# test what it will print when endpoint is called using postman software 
# and it can be access by typing 5000/item/<any string name>
# the <string name> will always goes to the getmethod parameter name as expected

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