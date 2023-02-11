from flask import Flask,request,jsonify,session
from flask_cors import *
import db
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/login",methods=['POST'])
def trylogin():
    print(request.json)
    username = request.json.get('username'),
    password = request.json.get('password'),
    print(username[0]),     
    print(password[0]),
    sql = f"SELECT * FROM stockproject.accounts where Email='{username[0]}';"
    datas = db.query_data(sql)
    password2 = datas[0]["Password"]
    print(password)
    print(password2)
    if(password2 == password[0]):
        
        json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
        return jsonify(json_result)
    else:
        return "true"




@app.route("/newuser", methods=['POST'])
def addNewUser():
    firstname = request.json.get('firstname'),
    lastname = request.json.get('lastname'),
    region = request.json.get('region'),
    bod = request.json.get('bod'),
    email = request.json.get('email'),
    password = request.json.get('password'),
    print(firstname)
    print(lastname)
    print(region)
    print(bod)
    print(email)
    print(password)
    sql = f"INSERT INTO `stockproject`.`accounts` (`FirstName`, `LastName`, `Region`, `Bod`, `Email`, `Password`, `LoginToken`) VALUES ('{firstname[0]}', '{lastname[0]}', '{region[0]}', '2023-2-7', '{email[0]}', '{password[0]}', 'zxcvbnmasdfghjklqwertyuiopasd');"
    db.insert_or_update_data(sql)
    json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
    return jsonify(json_result)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)
