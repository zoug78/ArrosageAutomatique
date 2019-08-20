from app import core
import logging
from flask_cors import CORS
from flask import Flask,request,jsonify

app = Flask(__name__)
CORS(app)

logging.basicConfig(filename='./log/arrosage.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

@app.route('/api/v1.0/arrosage/herbe', methods=['POST'])
def herbe():
    if request.json["action"] == "on":
        return { 'message' : core.main("on","herbe",request.json['temps'])}
    elif request.json["action"] == "off":
        return { 'message' : core.stop_gpio()}
    
@app.route('/api/v1.0/arrosage/potager', methods=['POST'])
def potager():
    if request.json["action"] == "on":
        return { 'message' : core.main("on","potager",request.json['temps'])}
    elif request.json["action"] == "off":
        return { 'message' : core.stop_gpio()}

@app.route('/api/v1.0/arrosage/status', methods=['GET'])
def status():
    return core.getStatus()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
