from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class Customer(Resource):
    def get(self):
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.customer()
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.customer()
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        pass

    def delete(self):
        pass