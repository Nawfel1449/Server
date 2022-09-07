from flask import Flask ,request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
api = Api(app)
from ART import *


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


@app.route('/SetTree',methods=['GET'])
def uploadTree():
    Tree   = request.args.get('tree')
    number = Tree.split(',')
    file = "tree_"
    print(file+str(len(number))+".json")
    DataToJson(number,file+str(len(number))+".json")
    return Tree


if __name__ == "__main__":
    app.run(debug=True)