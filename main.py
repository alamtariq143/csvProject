from flask import Flask, render_template, request
import os
import json
import datetime
import pymongo
from flask import jsonify
from bson import json_util

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

@app.route("/csv")
def csvDisplay():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.csvProject
    csvFile = request.args.get('csvName')
    print(csvFile)
    csvName = csvFile.split('.')
    csvCollectionName = csvName[0]
    print(csvCollectionName)
    collectionList = db.list_collection_names()
    output = []

    if csvCollectionName in collectionList:
        print("The collection exists.")
        collection = db[csvCollectionName]
        objects = collection.find({}, {'_id': False})
        return str(json.dumps({'results': list(objects)}, default = json_util.default, indent = 4))
        for x in collection.find():
            print(x)
            output.append(x)
    return("output")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
