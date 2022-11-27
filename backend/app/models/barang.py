import sys
sys.path.append('../models/app')
from ext import db

class barang(db.Model):
    barangid = db.Column("barangid", db.Integer, primary_key=True)
    nama = db.Column("nama", db.String(200))
    tipeid = db.Column("tipeid", db.ForeignKey('tipe.tipeid'), nullable=False)
    imagepath = db.Column("imagepath", db.String(500))
    satuan = db.Column("satuan", db.String(100))
    harga = db.Column("harga", db.Integer)
