from flask import Flask ,request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
api = Api(app)
from ART import *


@app.route('/', methods=['GET'])
def query_records():
    with open('EphKeys_512.json', 'r') as f:
        ID = request.args.get('ID')
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['ID'] == ID:
                return jsonify(record)
        return jsonify({'error': 'data not found'})


@app.route('/list', methods=['GET'])
def records():
    with open('EphKeys_1024.json', 'r') as f:
        IDs = request.args.get('ID')
        IDs = IDs.split(',')

        print(IDs)
        data = f.read()
        records = json.loads(data)
        keys = list()
        for ID in IDs :
            print(ID)
            for record in records:
                if record['ID'] == ID:
                    keys.append(record["PublicEphkey"])
        return jsonify(keys)


@app.route('/keys', methods=['GET'])
def keys():
    filename = "EphKeys_"
    numberOfKeys = request.args.get('keys')
    keyfile = filename + numberOfKeys + ".json"
    with open(keyfile, 'r') as f:
        data = f.read()
        records = json.loads(data)
        keys = list()
        for record in records:
            keys.append(record["PublicEphkey"])
        return jsonify(keys)



@app.route('/tree', methods=['GET'])
def Trees():
    filename = "Tree_"
    numberOfKeys = request.args.get('tree')
    keyfile = filename + numberOfKeys + ".json"
    with open(keyfile, 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)



#cant haldle request in 
@app.route('/SetTree',methods=['GET'])
def uploadTree():
    Tree   = request.args.get('tree')
    number = Tree.split(',')
    file = "tree_"
    print(file+str(len(number))+".json")
    DataToJson(number,file+str(len(number))+".json")
    return Tree

'''
@app.route('/SetTreeSetup',methods=['GET'])
def uploadsetup():
    setup   = request.args.get('tree')

    file = "setup_"
    print(file+str(len(number))+".json")
    DataToJson(setup,file+str(len(number))+".json")
    return Tree
'''

if __name__ == "__main__":
    app.run(debug=True)