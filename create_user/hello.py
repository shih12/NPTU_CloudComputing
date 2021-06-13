from typing import Collection
from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings
import hashlib
from pymongo import MongoClient
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
@app.route('/add', methods=['GET'])
def create_user_page():
    return render_template("creat_user.html")

# create user restful API
@app.route('/add', methods=['POST'])
@swag_from('apidocs/api_create_user.yml')
def create_user():
    client = MongoClient(host='rs3', port = 27043)
    db = client.test
    collection = db.account
    name = request.form['name']
    name = str(name)
        
    list = []
    for s in collection.find({"name": name}):
        list.append({"name": s['name']})

    if collection.find({"name": name}).count() >= 1:
        return render_template('fail.html')
    else:
        password = request.form['password']
        password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        
        logging.info('name:', name)
        logging.info('password:', password)

        message = dict()
        message['name'] = name
        message['password'] = password
        data = message
        # push name and password
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        message = json.dumps(message)
        logging.info('message:', message)

        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )

        connection.close()

        # reture requests
        # res = dict()
        # res['success'] = True
        # res['message'] = 'Create user successed, your name=' + name
        
        

        return render_template('success.html', data = data)



# @app.route('/')
# def index():
#     return 'Web App with Python Flask!'


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)