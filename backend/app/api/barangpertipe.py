from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class BarangPerTipe(Resource):
    def get(self):
        tipeid = request.args.get("tipeid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangPerTipe(tipeid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass