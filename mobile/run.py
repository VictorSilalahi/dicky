from flask import Flask, render_template, request, jsonify, session, redirect
import requests
from flask_cors import CORS
from urllib.parse import urlparse

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
app.secret_key = "iouceiouhcehochj0eojv0jerovjorijvoej4gf0j40gu480yg08hy408hyv408"
CORS(app)

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/tipe/<tipeid>', methods = ["GET"])
def pertipe(tipeid):
    r = requests.get("http://127.0.0.1:7000/api/barang/tipe?tipeid="+tipeid)
    if r.status_code == 200:
        temp = r.json()
        barang = temp["data"]
        hname = urlparse(request.base_url)
        return render_template("barang.html", data=barang, host = hname.hostname)
    else:
        return "Remote API Error!"

@app.route('/barang/<barangid>', methods = ["GET"])
def baranginfo(barangid):
    r = requests.get("http://127.0.0.1:7000/api/barang/info?barangid="+barangid)
    if r.status_code == 200:
        temp = r.json()
        barang = temp["data"]
        hname = urlparse(request.base_url)
        return render_template("infobarang.html", data=barang, host = hname.hostname)
    else:
        return "Remote API Error!"

@app.route('/bayar', methods = ["GET"])
def bayar():
    return render_template("bayar.html")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=1000)