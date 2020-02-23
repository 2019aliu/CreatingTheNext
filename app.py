import db
from flask import Flask, redirect, url_for, render_template, request, send_file, make_response
from socio_visual import do_plot
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/unemployment')
def unemployment():
    return render_template('unemployment.html')


@app.route('/homelessness')
def homeless():
    return render_template('homeless.html')


@app.route('/gdp')
def gdp():
    return render_template('gdp.html')


@app.route("/test")
def test():
    db.unemployment_data.collection.insert_one({"name": "John"})
    return "Connected to the data base!"


@app.route("/plot1")
def relplot1():
    bytes_obj = do_plot()
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')


@app.route("/global-unemployment")
def glob_unemp():
    return render_template('global-unemployment.html')


if __name__ == '__main__':
    app.run(port=8000)


