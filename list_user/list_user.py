from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
from werkzeug.utils import format_string
import pika
import logging
import warnings
from pymongo import MongoClient
import json
from flask_pymongo import PyMongo

# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

# setup flask app
app = Flask(__name__)

# setup swagger online document
swagger = Swagger(app)

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# create user restful API
@app.route('/list_user', methods=['GET'])
@app.route('/', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def create_user():

    client = MongoClient(host='rs3', port=27043)
    db = client.test
    collection = db.account

    data = []

    for s in collection.find():
        data.append({'name': s['name'], 'password': s['password']})
    
    return jsonify(data)
    



@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)
