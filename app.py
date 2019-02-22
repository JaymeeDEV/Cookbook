import os
from config import Config
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object(Config)

client = MongoClient(Config.MONGO_URI)
db = client.cookbookdb


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("index.html", recipes=db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
