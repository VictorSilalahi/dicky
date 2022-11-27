import sys
sys.path.append('../models/app')
from ext import db

class customer(db.Model):
    customerid = db.Column("customerid", db.Integer, primary_key=True)
    nama = db.Column("nama", db.String(200))
    ktp = db.Column("ktp", db.String(100))
    email = db.Column("email", db.String(100))
    pwd = db.Column("pwd", db.String(100))
