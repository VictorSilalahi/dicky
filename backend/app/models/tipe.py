import sys
sys.path.append('../models/app')
from ext import db

class tipe(db.Model):
    tipeid = db.Column("tipeid", db.Integer, primary_key=True)
    tipe = db.Column("tipe", db.String(200))
