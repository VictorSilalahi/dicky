from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi

class CartDetail(Resource):
    def get(self):
        cid = request.args.get("cid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.cartDetail(cid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})
    
    def post(self):
        cara = request.args.get("cara")
        cid = request.args.get("cid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.cartDetailLunas(cara, cid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        pass

    def delete(self):
        cid = request.args.get("cid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.cartDetailDel(cid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})
        