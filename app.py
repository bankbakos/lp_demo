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


if __name__ == '__main__':
    app.run(debug=True)
