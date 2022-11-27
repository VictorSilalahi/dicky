from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class Cart(Resource):
    def get(self):
        pass
    
    def post(self):
        tanggal = request.form['tanggal']
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.cart(tanggal)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        pass

    def delete(self):
        pass