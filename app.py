from flask import Flask ,request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def query_records():
    with open('EphKeys_1024.json', 'r') as f:
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




if __name__ == "__main__":
    app.run(debug=True)