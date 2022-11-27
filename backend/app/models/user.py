import sys
sys.path.append('../models/app')
from ext import db

class users(db.Model):
    userid = db.Column("userid", db.Integer, primary_key=True)
    nama = db.Column("nama", db.String(200))
    email = db.Column("email", db.String(100))
    pwd = db.Column("pwd", db.String(100))
    jenis = db.Column("jenis", db.String(100))    
