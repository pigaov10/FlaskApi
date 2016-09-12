#! /home/raphaeliarussi/virtualenvs/flask/bin/python2.7
import json
from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from flask import make_response
from bson import Binary, Code
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "logistica"

mongo = PyMongo(app, config_prefix='MONGO')

data = {}

class Provider(Resource):

    # todos
    def get(self):
        data = mongo.db.providers.find()
        if data.count() != 0:
            return dumps(data)
        else:
            return {'response': 'no provider found'}

class Index(Resource):
    def get(self):
        return redirect(url_for("providers"))

api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Provider, "/api/providers", endpoint="providers")

if __name__ == '__main__':
    app.run(debug=True)
