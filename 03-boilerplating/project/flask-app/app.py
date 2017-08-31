#!/usr/bin/env python
from flask import Flask, render_template, jsonify, request
from models.user import User
import random

app = Flask(__name__)
users = []
names = ["Tim", "Tom", "Bob", "Lisa", "Marie"]
domains = ["gmail.com", "web.de", "my.name", "yahoo.com"]

@app.route("/")
def index():
    return "Hello World"

@app.route("/inheritance")
def inherit():
    return render_template("child.html", title="Inheritance Rocks",
                           users=users)

@app.route("/user")
def get_user():
    if len(list(request.args.keys())) == 1:
        user_data = [u for u in users
                     if u.__getattribute__(list(request.args.keys())[0])
                     ==
                     request.args[list(request.args.keys())[0]]]

    else:
        user_data = users
    return render_template("user.html", users=user_data)

@app.route("/fancy")
def get_fancy():
    return jsonify(request.args)

def populate_users(n_user=3):
    for i in range(n_user):
        name = random.choice(names)
        age = random.randint(1, 100)
        email = ''.join([name.lower(),
                         str(age),
                         '@',
                         random.choice(domains)
                        ])
        u = User(name, age, email)
        users.append(u)
    for idx, u in enumerate(users):
        u.id = idx+1

if __name__ == "__main__":
    populate_users(10)
    app.run(debug=True)
