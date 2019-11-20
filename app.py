import os
from config import Config
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object(Config)

client = MongoClient(Config.MONGO_URI)
db = client.cookbookdb


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/products', methods=['POST', 'GET'])
def products():
    return render_template("products.html")


@app.route('/popular', methods=['POST', 'GET'])
def popular():
    return render_template("popular.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")

    """ Recipe Pages"""


@app.route('/chocolatebananasmoothie', methods=['POST', 'GET'])
def chocbansmoothie():
    return render_template("snacks/chocbansmoothie.html", recipes=db.recipes.find())


@app.route('/blueberrypancakes', methods=['POST', 'GET'])
def blueberrypancakes():
    return render_template("breakfast/blueberrypancakes.html", recipes=db.recipes.find())


@app.route('/broccolimacandcheese', methods=['POST', 'GET'])
def broccolimacandcheese():
    return render_template("dinner/brocmacandcheese.html", recipes=db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
