from flask_restful import Resource
from flask import request, jsonify
from ..db import koneksi
import time
import json

class Beli(Resource):
    def get(self):
        pass

    def post(self):
        nama = request.form["fullname"]
        # print(nama)
        email = request.form["email"]
        notelp = request.form["notelp"]
        daftarbeli = request.form["daftarbeli"]
        
        Koneksi  = koneksi.Koneksi()
        customerid = Koneksi.inputCustomer(nama, email, notelp)
        del Koneksi
        time.sleep(1)

        Koneksi  = koneksi.Koneksi()
        cartid = Koneksi.inputCart(customerid)
        del Koneksi
        time.sleep(1)

        db = json.loads(daftarbeli)
        Koneksi  = koneksi.Koneksi()
        ret = Koneksi.inputPembelian(cartid, db)
        del Koneksi

        return jsonify({"msg":"ok", "data":ret})
    
    def put(self):
        pass

    def delete(self):
        pass