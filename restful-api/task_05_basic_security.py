#!/usr/bin/python3
"""
Module
"""


from flask import Flask, jsonfy, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config['S_KEY'] = 'Secret_key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user[password], password):
        return user
    else:
        return None


@app.route('/basic-protecter')
@auth.login_required
def basic_protecter():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_tok = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonfy(access_tok=access_tok)
    else:
        return jsonfy({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonfy({"error": "Admin access requiered"}), 403
    else:
        return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonfy({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonfy({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonfy({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonfy({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonfy({"error": "Fresh token requiered"}), 401


if __name__ == "__main__":
    app.run()
