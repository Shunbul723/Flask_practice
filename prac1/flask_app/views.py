from flask_app import app
from flask import request,jsonify
from flask_app import controllers

@app.route('/')
def page():
    return "Welcome Home"

@app.route('/insert',methods=['POST'])
def post_data():
    data=request.get_json()
    res=controllers.post_controllers(data)
    return jsonify(message=res)