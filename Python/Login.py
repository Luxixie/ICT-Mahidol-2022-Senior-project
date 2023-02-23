from crypt import methods
from re import A
from flask import Flask,request,jsonify,session
from flask_cors import *
import db
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/login",methods=['POST'])
def trylogin():
    print(request.json)
    email = request.json.get('email'),
    password = request.json.get('password'),
    print(email[0]),     
    print(password[0]),
    sql = f"SELECT * FROM stockproject.accounts where Email='{email[0]}';"
    datas = db.query_data(sql)
    password2 = datas[0]["Password"]
    print(password)
    print(password2)
    if(password2 == password[0]):
        accountid = datas[0]["AccountId"]
        username = datas[0]["FirstName"]+datas[0]["LastName"]
        region = datas[0]["Region"]
        birthdate = datas[0]["BOD"]
        email = datas[0]["Email"]
        json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","accountid":accountid, "username":username,"region":region,"birthdate":birthdate,"email":email}}
        print(json_result)
        return jsonify(json_result)
    else:
        return "true"




@app.route("/signup", methods=['POST'])
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

@app.route("/editprofile", methods=['POST'])
def edituser():
    accountid = ["AccountId"],
    firstname = request.json.get('firstname'),
    lastname = request.json.get('lastname'),
    region = request.json.get('region'),
    bod = request.json.get('bod'),
    email = request.json.get('email'),
    print(accountid)
    print(firstname)
    print(lastname)
    print(region)
    print(bod)
    print(email)
    sql = f"UPDATE stockproject SET `accounts` (`FirstName`, `LastName`, `Region`, `Bod`, `Email`, `LoginToken`) VALUES ('{firstname[0]}', '{lastname[0]}', '{region[0]}', '2023-2-7', '{email[0]}', 'zxcvbnmasdfghjklqwertyuiopasd' WHERE AccountId = {accountid[0]};"
    db.insert_or_update_data(sql)
    json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
    return jsonify(json_result)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)
