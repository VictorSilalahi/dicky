import sqlite3
import os.path
from flask import jsonify
from datetime import datetime
import json

BASE_DIR = ""

class Koneksi:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        dbMaster = BASE_DIR + '\\master.db'
        self.conn = sqlite3.connect(dbMaster)
    
    def validasi(self, uname, pwd):
        temp = self.conn.execute("select count(*) as jlh from tusers where email='"+uname+"' and pwd='"+pwd+"'")
        res = temp.fetchone()
        if res[0]!=1:
            return 0
        else:
            return 1

    # model : tipe
    def tipe(self):
        data = []
        temp = self.conn.execute("select * from ttipe")
        rows = temp.fetchall()
        for r in rows:
            data.append({"tipeid":r[0],"tipe":r[1], "path":"static/images/tipe.png"})
        return data

    def tipeAdd(self, tipe):
        self.conn.execute("insert into ttipe (tipe) values ('"+tipe+"')")
        self.conn.commit()
        return "ok"

    def tipeDel(self, tipe):
        self.conn.execute("delete from ttipe where tipeid="+tipe)
        self.conn.commit()
        return "ok"

    def tipeSaveEdit(self, tipe, tipeid):
        self.conn.execute("update ttipe set tipe='"+tipe+"' where tipeid="+tipeid)
        self.conn.commit()
        return "ok"

    # model : barang
    def barang(self):
        data = []
        temp = self.conn.execute("select tbarang.barangid, tbarang.nama, tbarang.satuan, tbarang.jumlah, tbarang.harga, ttipe.tipe from tbarang, ttipe where tbarang.tipeid=ttipe.tipeid order by ttipe.tipe")
        rows = temp.fetchall()
        for r in rows:
            data.append({"barangid":r[0],"nama":r[1],"satuan":r[2],"jumlah":r[3],"harga":r[4], "tipe":r[5]})
        return data

    def barangPerTipe(self, tipeid):
        data = []
        temp = self.conn.execute("select tbarang.barangid, tbarang.nama, tbarang.satuan, tbarang.jumlah, tbarang.harga, tbarang.desc, tbarang.path from tbarang, ttipe where tbarang.tipeid=ttipe.tipeid and ttipe.tipeid="+tipeid)
        rows = temp.fetchall()
        for r in rows:
            data.append({"barangid":r[0],"nama":r[1],"satuan":r[2],"jumlah":r[3],"harga":r[4], "ket":r[5], "path":r[6] })
        return data

    def barangInfo(self, barangid):
        data = []
        temp = self.conn.execute("select tbarang.barangid, tbarang.nama, tbarang.satuan, tbarang.jumlah, tbarang.harga, tbarang.desc, tbarang.path from tbarang where tbarang.barangid="+barangid)
        rows = temp.fetchall()
        for r in rows:
            data.append({"barangid":r[0],"nama":r[1],"satuan":r[2],"jumlah":r[3],"harga":r[4], "ket":r[5], "path":r[6] })
        return data

    def barangAdd(self, nama, satuan, tipe, jumlah, harga, ket, fileGbr):
        self.conn.execute("insert into tbarang (nama, satuan, tipeid, jumlah, harga, desc, path) values ('"+nama+"','"+satuan+"',"+tipe+","+jumlah+","+harga+",'"+ket+"','static/images/barang/"+fileGbr+"')")
        self.conn.commit()
        return "ok"

    def barangDel(self, barangid):
        self.conn.execute("delete from tbarang where barangid="+barangid)
        self.conn.commit()
        return "ok"

    def barangSaveEdit(self, nama, satuan, tipeid, barangid):
        self.conn.execute("update tbarang set nama='"+nama+"', satuan='"+satuan+"', tipeid="+tipeid+" where barangid="+barangid)
        self.conn.commit()
        return "ok"

    def barangHargaSave(self, harga, barangid):
        self.conn.execute("update tbarang set harga="+harga+" where barangid="+barangid)
        self.conn.commit()
        return "ok"

    def barangJumlahSave(self, jumlah, barangid):
        self.conn.execute("update tbarang set jumlah="+jumlah+" where barangid="+barangid)
        self.conn.commit()
        return "ok"

    # model : customer
    def customer(self):
        data = []
        temp = self.conn.execute("select * from tcustomer")
        rows = temp.fetchall()
        for r in rows:
            data.append({"customerid":r[0],"fullname":r[1],"email":r[2],"alamat":r[3],"notelp":r[4]})
        return data

    # model : report
    def report(self, bln, thn, cara):
        data = []
        temp = self.conn.execute("select tcart.cartid, sum(tcartdesc.total), tcart.tanggal, tcustomer.fullname from tcart, tcartdesc, tcustomer where  tcart.customerid=tcustomer.customerid and tcart.cartid=tcartdesc.cartid and strftime('%m', tcart.tanggal) = '"+bln+"' and strftime('%Y', tcart.tanggal) = '"+thn+"' and tcart.jenisbayar='"+cara+"' order by tcart.tanggal")
        rows = temp.fetchall()
        for r in rows:
            data.append({"tanggal":r[2],"total":r[1],"nama":r[3]})
        return data

    # pembelian
    def inputCustomer(self, fullname, email, notelp):
        curr = self.conn.cursor()
        temp = curr.execute("insert into tcustomer (fullname, email, notelp) values ('"+fullname+"','"+email+"','"+notelp+"')")
        last_id = temp.lastrowid
        self.conn.commit()
        return last_id

    def inputCart(self, customerid):
        tanggal = datetime.now()
        tgl = tanggal.strftime("%Y-%m-%d")
        curr = self.conn.cursor()
        temp = curr.execute("insert into tcart (customerid, tanggal) values ("+str(customerid)+",'"+tgl+"')")
        last_cart_id = temp.lastrowid
        self.conn.commit()
        return last_cart_id

    def inputPembelian(self, cartid, db):
        newdb = json.loads(db)
        for d in newdb:
            self.conn.execute("insert into tcartdesc (cartid, barangid, jumlah, total) values ("+str(cartid)+","+str(d[1])+","+str(d[3])+","+str(d[4])+")")
        self.conn.commit()
        return "ok"

    # model : cart
    def cart(self, tanggal):
        data = []
        temp = self.conn.execute("SELECT tcart.cartid, tcustomer.fullname, tcustomer.notelp, tcustomer.email from tcustomer, tcart where tcustomer.customerid=tcart.customerid and tcart.tanggal='"+tanggal+"' and tcart.telahdibayar is null")
        rows = temp.fetchall()
        for r in rows:
            temp2 = self.conn.execute("SELECT count(*) from tcart, tcustomer where tcart.customerid=tcustomer.customerid and tcustomer.email='"+r[3]+"' and tcart.telahdibayar='y'")
            rows2 = temp2.fetchone()
            data.append({"cartid":r[0], "fullname":r[1],"telp":r[2],"email":r[3], "jumlahbeli": rows2[0]})
        return data

    def cartDetail(self, cid):
        data = []
        temp = self.conn.execute("SELECT tcartdesc.cartdescid, tbarang.nama, tcartdesc.jumlah, tcartdesc.total from tcartdesc, tbarang where tcartdesc.barangid=tbarang.barangid and tcartdesc.cartid="+cid)
        rows = temp.fetchall()
        for r in rows:
            data.append({"cartdescid":r[0], "nama":r[1], "jumlah":r[2], "total": r[3]})
        return data

    def cartDetailLunas(self, cara, cid):
        data = []
        temp = self.conn.execute("SELECT tcartdesc.cartdescid, tcartdesc.barangid, tcartdesc.jumlah from tcartdesc, tbarang where tcartdesc.barangid=tbarang.barangid and tcartdesc.cartid="+cid)
        rows = temp.fetchall()
        for r in rows:
            self.conn.execute("update tbarang set jumlah=jumlah - "+str(r[2])+" where barangid="+str(r[1]))
            self.conn.commit()
        self.conn.execute("update tcart set telahdibayar='y', jenisbayar='"+cara+"' where cartid="+cid)
        self.conn.commit()
        return "ok"

    def cartDetailDel(self, cid):
        self.conn.execute("delete from tcart where cartid="+cid)
        self.conn.commit()
        return "ok"

    def __del__(self):
        self.conn.close()