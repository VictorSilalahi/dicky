from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class Customercheck(Resource):
    def get(self):
        pass

    def post(self):
        email = request.form["email"]
        notelp = request.form["notelp"]

        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.customervalidasi(email,notelp)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        pass

    def delete(self):
        pass