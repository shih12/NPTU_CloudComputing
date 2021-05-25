
from flask import Flask,request
import json
import publisher


app = Flask(__name__)
@app.route('/get_helloworld', methods=['GET'])
def get_hello_world():
    return 'hello world'

@app.route('/post_helloworld', methods=['POST'])
def post_helloworld():
    jsonobj = request.get_json(silent=True)
    token = json.dumps(jsonobj['token']).replace("\"", "")
    publisher.publish(token)

    return token

@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)