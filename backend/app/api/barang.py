from flask_restful import Resource
from flask import request, jsonify
import os
from werkzeug.utils import secure_filename
from ..db import koneksi

class Barang(Resource):
    def get(self):
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barang()
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def post(self):
        nama = request.form["nama"]
        satuan = request.form["satuan"]
        tipe = request.form["tipe"]
        jumlah = request.form["jumlah"]
        harga = request.form["harga"]
        ket = request.form["ket"]
        fileGbr = request.files.get("fileGambar")
        namaGbr = secure_filename(fileGbr.filename)
        fileGbr.save(os.path.join("./app/static/images/barang/", namaGbr))
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangAdd(nama, satuan, tipe, jumlah, harga, ket, namaGbr)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def put(self):
        nama = request.args.get("nama")
        satuan = request.args.get("satuan")
        tipeid = request.args.get("tipeid")
        barangid = request.args.get("barangid")
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangSaveEdit(nama, satuan, tipeid, barangid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})

    def delete(self):
        barangid = request.args.get('barangid')
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.barangDel(barangid)
        del Koneksi
        return jsonify({"msg":"ok", "data":ret})
