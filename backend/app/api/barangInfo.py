from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class BarangInfo(Resource):
    def get(self):
        barangid = request.args.get("barangid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangInfo(barangid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass