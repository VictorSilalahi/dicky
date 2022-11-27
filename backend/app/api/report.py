from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class Report(Resource):
    def get(self):
        bln = request.args.get("bln")
        thn = request.args.get("thn")
        cara = request.args.get("cara")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.report(bln, thn, cara)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass