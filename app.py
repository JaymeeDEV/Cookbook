import os
from config import Config
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object(Config)

client = MongoClient(Config.MONGO_URI)
db = client.cookbookdb

"""
User Authentication
"""


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/popular')
def popular():
    return render_template("popular.html")


@app.route('/register')
def register():
    return render_template("register.html", methods=['POST', 'GET'])


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
