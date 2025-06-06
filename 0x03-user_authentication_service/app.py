#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route("/", methods=['GET'])
def home():
    """Route that returns a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """Route that registers users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def login():
    """Log in user and create a session."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not auth.valid_login(email, password):
        abort(401)

    session_id = auth.create_session(email)
    if not session_id:
        abort(401)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logsout the user by destroying session"""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)
    user = auth.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    auth.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """Return user profile"""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)
    user = auth.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Handles password reset token generation"""
    email = request.form.get('email')
    try:
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        return abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """reset password endpoint to update user passwd"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if not email or not reset_token or not new_password:
        abort(400)

    try:
        auth.update_password(reset_token, new_password)
    except Exception:
        abort(403)

    return jsonify({"email": email, "message": "password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
