from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class BarangHarga(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        harga = request.args.get("harga")
        barangid = request.args.get("barangid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangHargaSave(harga, barangid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def delete(self):
        pass