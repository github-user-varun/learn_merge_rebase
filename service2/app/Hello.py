from flask import Flask
from flask import request, Response
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['GET', 'POST'])
def assetcompliance():
    if request.method == 'GET':
        return "Root Page"

@app.route('/hello', methods=['GET', 'POST'])
def assetcompliance_hello():
    if request.method == 'GET':
        return "Hello World Page Service 2 feature1"

@app.route('/feature1', methods=['GET', 'POST'])
def assetcompliance_hello():
    if request.method == 'GET':
        return "Hello World Page service 1 feature1 branch"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5053)
