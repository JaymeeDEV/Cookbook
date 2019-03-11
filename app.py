import os
from config import Config
from flask import Flask, render_template, redirect, request, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config.from_object(Config)

client = MongoClient(Config.MONGO_URI)
db = client.cookbookdb


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/popular')
def popular():

    return render_template("popular.html", recipes=db.recipes.find())


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_in_db = db.users.find_one({
            "username": request.form['username']
        })
        print(user_in_db)
        if user_in_db and check_password_hash(user_in_db['password'], request.form['password']):
            session["username"] = user_in_db["username"]
            return redirect(url_for('index'))
        else:
            db.users.insert_one({
                "username": request.form['username'],
                "email": request.form['email'],
                "password": generate_password_hash(request.form['password'])
            })
            return redirect(url_for('index'))
    else:
        return render_template("register.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
