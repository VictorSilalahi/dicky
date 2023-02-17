from flask import Flask, render_template, request, jsonify, session, redirect
import requests
from flask_cors import CORS

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
app.secret_key = "iouceiouhcehochj0eojv0jerovjorijvoej4gf0j40gu480yg08hy408hyv408"
CORS(app)

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/validate', methods = ["POST"])
def validasi():
    uname = request.form["txtUsername"]
    pwd = request.form['txtPassword']
    
    # Send POST request (validasi)
    r = requests.post("http://127.0.0.1:7000/api/user/validate", data={"username":uname,"password":pwd}, verify=False)

    if r.status_code == 200:
        temp = r.json()
        if temp['data'] == 1:
            session['adminlogin'] = True
            return redirect("/tipe") 
        else:
            return redirect("/") 
    else:
        return "Remote API Error!"

@app.route('/tipe', methods = ["GET", "POST"])
def tipe(): 
    if session.get('adminlogin') == None:
        return redirect("/")   
    if session['adminlogin'] == False:
        return redirect("index.html")   
    if session['adminlogin'] == True:
        return render_template("tipe.html")

@app.route('/barang', methods = ["GET", "POST"])
def barang(): 
    if session.get('adminlogin') == None:
        return redirect("/")   
    if session['adminlogin'] == False:
        return redirect("index.html")   
    if session['adminlogin'] == True:
        return render_template("barang.html")

@app.route('/pembelian', methods = ["GET", "POST"])
def pembelian(): 
    if session.get('adminlogin') == None:
        return redirect("/")   
    if session['adminlogin'] == False:
        return redirect("index.html")   
    if session['adminlogin'] == True:
        return render_template("pembelian.html")

@app.route('/report', methods = ["GET", "POST"])
def report(): 
    if session.get('adminlogin') == None:
        return redirect("/")   
    if session['adminlogin'] == False:
        return redirect("index.html")   
    if session['adminlogin'] == True:
        return render_template("report.html")

@app.route('/logoff', methods = ["GET", "POST"])
def logoff():
    session.clear()
    return render_template("index.html") 

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)