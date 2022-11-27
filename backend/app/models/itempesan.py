import sys
sys.path.append('../models/app')
from ext import db

class itempesan(db.Model):
    itempesanid = db.Column("userid", db.Integer, primary_key=True)
    pemesananid = db.Column("pemesananid", db.ForeignKey('pemesanan.pemesananid'), nullable=False)
    barangid = db.Column("barangid", db.ForeignKey('barang.barangid'), nullable=False)
    jumlah = db.Column("jumlah", db.Integer)
    harga = db.Column("harga", db.Integer)
    total = db.Column("total", db.Integer)
