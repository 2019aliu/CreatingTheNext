import db
from flask import Flask, redirect, url_for, render_template, request, send_file, make_response
from socio_visual import do_plot
import io
import base64
import matplotlib.pyplot as plt
import urllib.parse
import pandas as pd
app = Flask(__name__)
PORT = 8000

@app.route('/')
def index():
    bytes_obj = do_plot()
    plot_url = urllib.parse.quote(base64.b64encode(bytes_obj.read()).decode())
    return render_template('index.html', plot_url=plot_url)


@app.route('/unemployment')
def unemployment():
    return render_template('unemployment.html')


@app.route('/homelessness')
def homeless():
    return render_template('homeless.html')


@app.route('/gdp')
def gdp():
    return render_template('county-unemployment.html')


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


def do_plot():
    # img = StringIO()
    bytes_image = io.BytesIO()
    y = [1, 2, 3, 4, 5]
    x = [0, 2, 1, 3, 4]

    plt.plot(x, y)
    plt.savefig(bytes_image, format='png')
    plt.close()
    bytes_image.seek(0)
    return bytes_image

    # unemploymentCollection = db.getCollection("unemployment_rate")
    # df_unrate = pd.DataFrame(list(unemploymentCollection.find())
    # plt.plot()


if __name__ == '__main__':
    app.run(port=PORT)


