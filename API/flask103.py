# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:58:35 2022

@author: mingt
"""

# simulate an online store
 
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

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

@app.route('/')
def home():
  return render_template('index.html')
 
# We will get the name of store to create (POST) 
# and send the name list back (GET) 

# POST /store dataL {name:}
@app.route('/store', methods = ['POST']) # by default is a GET request, the endpoint can be accesiable bia GET and POST in the sametime
def create_a_store():
    request_data = request.get_json() # all us to get the data back
    new_store = {
        'name': request_data['name'],
        'items': []             
        }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def print_a_store_name(name): # parameter match above; cosnider /store/name_A, then the name will be matched to 'name_A'
    for store_i in stores:
        if store_i['name'] == name:
            return jsonify(store_i)
    return jsonify({'message': 'store not found'})
    
# GET /store
@app.route('/store')
def print_store_list(): 
    return jsonify({'stores': stores}) 

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_from_a_store(name):
    request_data = request.get_json()
    for store_i in stores:
        if store_i['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']          
                }
            store_i['items'].append(new_item)
            return jsonify(new_item) # or the store
    return jsonify({'message': 'store not found'})
            

# GET /store//<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_from_a_store(name):
    for store_i in stores:
        if store_i['name'] == name:
            return jsonify({'items': store_i['items']})
    return jsonify({'message': 'store not found'})
    
app.run(port = 4998)

