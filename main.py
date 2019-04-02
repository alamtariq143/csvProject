from flask import Flask, render_template
import os
import json
import datetime
import pymongo
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/apiListCSV")
def listing():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.csvProject
    collection = db.masterCSV
    output = []
    for cursor in collection.find():
        output.append({'title':cursor['title'],'list':cursor['listOfCSV']})
        return jsonify(output)

    return("some json")

if __name__ == "__main__":
    app.run(debug=True)
