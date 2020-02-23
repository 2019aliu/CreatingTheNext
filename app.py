import db
from flask import Flask, redirect, url_for, render_template, request
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

if __name__ == '__main__':
    app.run(port=8000)


