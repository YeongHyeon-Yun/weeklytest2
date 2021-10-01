from flask import Flask, render_template, jsonify, request
import datetime
app = Flask(__name__)

import requests

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles':articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']


    title = url_receive
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    description = comment_receive


    doc = {
        'title':title,
        'date': nowDatetime,
        'description':description,
        'comment':comment_receive
    }

    db.articles.insert_one(doc)

    return jsonify({'msg':'저장이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)