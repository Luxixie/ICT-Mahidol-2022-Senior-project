from flask import Flask, jsonify
from flask_cors import *
import db
import json


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/quiz')
def get_questions():

    sql = f"Multiple_choiceID,chapterid,question, option_a, option_b, option_c, option_d, answer FROM stockproject.Multiple_choice"
    datas = db.query_data(sql)
    print(datas)
    return jsonify(datas)



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8087)
