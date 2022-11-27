from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class BarangJumlah(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        jumlah = request.args.get("jumlah")
        barangid = request.args.get("barangid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangJumlahSave(jumlah, barangid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def delete(self):
        pass