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
    popular_recipe_ids=[ObjectId("5c6ef1771c9d440000dc9420"),
                        ObjectId("5c87dd651c9d440000a8301b"),
                        ObjectId("5e1b911e1c9d44000048fa7e")]
    popular_recipes=db.recipes.find({"_id":ObjectId("5c6ef1771c9d440000dc9420"),
                                     "_id":ObjectId("5c87dd651c9d440000a8301b"),
                                     "_id":ObjectId("5e1b911e1c9d44000048fa7e")})
    return render_template("index.html", popular_recipes=popular_recipes)


@app.route('/products', methods=['POST', 'GET'])
def products():
    return render_template("products.html")


@app.route('/popular', methods=['POST', 'GET'])
def popular():
    return render_template("popular.html")


@app.route('/breakfast', methods=['POST', 'GET'])
def breakfast():
    return render_template("breakfast.html")


@app.route('/lunch', methods=['POST', 'GET'])
def lunch():
    return render_template("lunch.html")


@app.route('/dinner', methods=['POST', 'GET'])
def dinner():
    return render_template("dinner.html")


    """ Recipe Pages"""

# Snacks
@app.route('/chocolatebananasmoothie', methods=['POST', 'GET'])
def chocbansmoothie():
    return render_template("snacks/chocbansmoothie.html", recipes=db.recipes.find())


@app.route('/perfectpancakes', methods=['POST', 'GET'])
def perfectpancakes():
    return render_template("snacks/perfectpancakes.html", recipes=db.recipes.find())


@app.route('/hotcrossbuns', methods=['POST', 'GET'])
def hotcrossbuns():
    return render_template("snacks/hotcrossbuns.html", recipes=db.recipes.find())

# Breakfast
@app.route('/blueberrypancakes', methods=['POST', 'GET'])
def blueberrypancakes():
    return render_template("breakfast/blueberrypancakes.html", recipes=db.recipes.find())


@app.route('/chocolatebananaporridge', methods=['POST', 'GET'])
def chocolatebananaporridge():
    return render_template("breakfast/chocobanporridge.html", recipes=db.recipes.find())


@app.route('/breakfastberryparfait', methods=['POST', 'GET'])
def breakfastberryparfait():
    return render_template("breakfast/berryparfait.html", recipes=db.recipes.find())

# Lunch
@app.route('/cauliflowercheesesoup', methods=['POST', 'GET'])
def cauliflowercheesesoup():
    return render_template("lunch/caulicheesesoup.html", recipes=db.recipes.find())


@app.route('/wildricesalad', methods=['POST', 'GET'])
def wildricesalad():
    return render_template("lunch/wildricesalad.html", recipes=db.recipes.find())


@app.route('/crunchypestochicken', methods=['POST', 'GET'])
def crunchypestochicken():
    return render_template("lunch/pestochickencous.html", recipes=db.recipes.find())

# Dinner
@app.route('/broccolimacandcheese', methods=['POST', 'GET'])
def broccolimacandcheese():
    return render_template("dinner/brocmacandcheese.html", recipes=db.recipes.find())


@app.route('/chickenstew', methods=['POST', 'GET'])
def chickenstew():
    return render_template("dinner/chickenstew.html", recipes=db.recipes.find())


@app.route('/steakandpotato', methods=['POST', 'GET'])
def steakandpotato():
    return render_template("dinner/steakpotato.html", recipes=db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
