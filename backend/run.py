from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from ext import db

from app.api.user import User
from app.api.tipe import Tipe
from app.api.barang import Barang
from app.api.barangJumlah import BarangJumlah
from app.api.barangHarga import BarangHarga
from app.api.barangpertipe import BarangPerTipe
from app.api.barangInfo import BarangInfo
from app.api.customer import Customer
from app.api.customercheck import Customercheck
from app.api.cart import Cart
from app.api.cartdetail import CartDetail
from app.api.beli import Beli
from app.api.reporttahunan import ReportTahunan
from app.api.reportbulanan import ReportBulanan
from app.api.reportpembelitahunan import ReportPembeliTahunan

api = None

def createApp():
    app = Flask(__name__, static_folder='app/static', template_folder='app/templates')

    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_PATH'] = 'static/images/barang'
    
    # api list
    api = Api(app)
    api.add_resource(User, "/api/user/validate")
    api.add_resource(Tipe, "/api/tipe")
    api.add_resource(Customer, "/api/customer")
    api.add_resource(Customercheck, "/api/customer/check")
    api.add_resource(Barang, "/api/barang")
    api.add_resource(BarangPerTipe, "/api/barang/tipe")
    api.add_resource(BarangJumlah, "/api/barang/jumlah")
    api.add_resource(BarangHarga, "/api/barang/harga")
    api.add_resource(BarangInfo, "/api/barang/info")
    api.add_resource(Cart, "/api/cart")
    api.add_resource(CartDetail, "/api/cart/detail")
    api.add_resource(Beli, "/api/beli")
    api.add_resource(ReportTahunan, "/api/reporttahunan")
    api.add_resource(ReportBulanan, "/api/reportbulanan")
    api.add_resource(ReportPembeliTahunan, "/api/reportpembelitahunan")

    CORS(app)

    return app

if __name__=="__main__":
    app = createApp()
    app.run(debug=True, host="0.0.0.0", port=7000)