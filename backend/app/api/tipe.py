from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class Tipe(Resource):
    def get(self):
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.tipe()
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        tipe = request.form["namatipe"]
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.tipeAdd(tipe)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        tipeid = request.args.get('tipeid')
        tipe = request.args.get('nama')
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.tipeSaveEdit(tipe,tipeid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def delete(self):
        tipeid = request.args.get('tipeid')
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.tipeDel(tipeid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})
