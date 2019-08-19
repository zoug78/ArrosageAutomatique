import core
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/api/v1.0/arrosage/herbe', methods=['POST'])
def herbe():
    if request.json["action"] == "on":
        return core.main("on","herbe",request.json['temps'])
    elif request.json["action"] == "off":
        return core.stop_gpio()
    
@app.route('/api/v1.0/arrosage/potager', methods=['POST'])
def potager():
    if request.json["action"] == "on":
        return core.main("on","potager",request.json['temps'])
    elif request.json["action"] == "off":
        return core.stop_gpio()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
