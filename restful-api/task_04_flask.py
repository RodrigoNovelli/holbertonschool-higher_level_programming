#!/usr/bin/python3


'''
In this module we are making
a simple API with flask
'''


from flask import Flask, jsonify, request


app = Flask(__name__)
users_list = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data")
def data():
    return jsonify(list(users_list.keys())), 200


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def users(username):
    username_ = users_list.get(username)
    if username_:
        return jsonify(username_), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add():
    new_user = request.get_json()
    user = new_user['username']
    name = new_user['name']
    age = new_user['age']
    city = new_user['city']
    if not isinstance(user, str) or not user:
        return jsonify({"error": "Username is required"}), 400
    users_list[user] = {"city": city, "age": age,
                        "name": name, "username": user}
    message = {"message": "User added", "user": users_list[user]}
    return jsonify(message), 201


if __name__ == "__main__":
    app.run()
