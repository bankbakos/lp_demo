from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route("/time")
def time():
    return render_template("time.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/addtocart")
def add_to_cart():
    return render_template("addtocart.html")

@app.route('/cartvalue')
def payment():
    return render_template("cartvalue.html")

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/tobi')
def tobi():
    return render_template("tobi.html")

@app.route('/engagement')
def engagement():
    return render_template("engagement.html")

@app.route('/echo')
def echo():
    return render_template("echo.html")

@app.route('/auth')
def auth():
    return render_template("auth.html")

@app.route('/noauth')
def noauth():
    return render_template("noauth.html")


@app.route('/sim')
def sim():
    return render_template("sim.html")


@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/sales')
def sales():
    return render_template("sales.html")

@app.route('/kosaram')
def kosaram():
    return render_template("kosaram.html")

@app.route('/sales/kosaram')
def kosaramsales():
    return render_template("kosaramsales.html")

@app.route('/vhub')
def vhub():
    return render_template("vhub.html")

@app.route('/mobil')
def mobil():
    return render_template("mobil_payment.html")

@app.route('/fixbilling')
def fixbilling():
    return render_template("fixbilling.html")


@app.route('/tobigtp')
def tobigtp():
    return render_template("tobigtp.html")

@app.route('/tobigtp2')
def tobigtp2():
    return render_template("tobigtp2.html")

@app.route('/persinfo')
def persinfo():
    return render_template("persinfo.html")

@app.route('/persinfo_prod')
def persinfoprod():
    return render_template("persinfo_prod.html")

@app.route('/screenshare')
def screenshare():
    return render_template("screenshare.html")

@app.route('/mvm')
def screenshare():
    return render_template("MVM.html")
    
@app.route('/vfh_virtus')
def vfh_virtus():
    return render_template("vfh_virtus.html")

@app.route('/vfh_virtus_prod')
def vfh_virtus_prod():
    return render_template("vfh_virtus_prod.html")

if __name__ == '__main__':
    app.run(debug=True)
