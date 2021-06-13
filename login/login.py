from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import hashlib
# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)

swagger = Swagger(app)


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']

    # Database connect
    client = MongoClient(host='rs2', port = 27042)
    db = client.test
    collection = db.account

    # var chang str 
    name = str(name)
    password = str(hashlib.sha1(password.encode('utf-8')).hexdigest())

    list =[]
    for s in collection.find({"name": name, "password": password}):
        list.append({"name": s['name'], "password": s['password']})
    if len(list) == 1:
        rs = requests.Session()
        payload = {
            "from":"bbs/Gossiping/index.html",
            "yes":"yes"
        }
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        url = "https://www.ptt.cc/bbs/Gossiping/index.html"
        
        data_list = []
        for i in range(3):
            res = rs.get(url)
            soup = BeautifulSoup(res.text,"html.parser")
            sel = soup.select("div.title a")
            u = soup.select("div.btn-group.btn-group-paging a")
            url = "https://www.ptt.cc"+u[1]["href"]
            for s in sel:
                data_list.append({'url':"https://www.ptt.cc"+s["href"],'title':s.text})
        time = len(data_list)
        # s = json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)
        
        return render_template('data.html',data = data_list,time = time)
    else:
        return "Login Error"


# @app.route('/')

# def index():
#     return 'Web App With Python Flask!'


app.run(host='0.0.0.0',port=5005)