import sys
sys.path.append('../models/app')
from ext import db

class pemesanan(db.Model):
    pemesananid = db.Column("pemesananid", db.Integer, primary_key=True)
    customerid = db.Column("customerid", db.ForeignKey('customer.customerid'), nullable=False)
    tanggal = db.Column("tanggal", db.DateTime())
    totalbayar = db.Column("totalbayar", db.Integer)
