from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class User(Resource):
    def get(self):
        pass

    def post(self):
        uname = request.form["username"]
        pwd = request.form["password"]

        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.validasi(uname, pwd)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        pass

    def delete(self):
        pass