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

@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
