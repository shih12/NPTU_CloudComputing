from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json

# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)

swagger = Swagger(app)


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 


@app.route('/login', methods=['POST'])
@app.route('/',methods=['POST'])
@swag_from('apidocs/api_create_user.yml')
def login():
    rs = requests.Session()
    payload = {
        "from":"bbs/Gossiping/index.html",
        "yes":"yes"
    }
    res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"

    # retrive post body
    jsonobj = request.get_json(silent=True)
    username = json.dumps(jsonobj['username']).replace("\"", "")
    password = json.dumps(jsonobj['password']).replace("\"", "")


    client = MongoClient(host='rs2', port = 27042)
    db = client.test
    collection = db.account
    username = str(username)
    password = str(password)

    list =[]
    for s in collection.find({"name": username, "password": password}):
        list.append({"name": s['name'], "password": s['password']})
        
    if len(list) > 0:
        url = "https://www.ptt.cc/bbs/Gossiping/index.html"
        data = []
        for i in range(3):

            res = rs.get(url)
            soup = BeautifulSoup(res.text,"html.parser")
            sel = soup.select("div.title a")
            u = soup.select("div.btn-group.btn-group-paging a")
            url = "https://www.ptt.cc"+u[1]["href"]
            
            for s in sel:
                data.append({'url': "https://www.ptt.cc"+s["href"], 'title':s.text})

        s = json.dumps(data,ensure_ascii=False)

        return jsonify(s)
    else:
        return "account error"
    
    return jsonify(len(data))


@app.route('/')

def index():
    return 'Web App With Python Flask!'


app.run(host='0.0.0.0',port=5005)