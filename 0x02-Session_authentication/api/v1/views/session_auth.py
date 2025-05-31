#!/usr/bin/env python3
"""Session Authentication views"""


from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """Login route to log in with session auth"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = os.getenv("SESSION_NAME", "_my_session_id")
    response.set_cookie(session_name, session_id)

    return response


@app_views.route(
        'auth_session/logout', methods=['DELETE'],
        strict_slashes=False
        )
def sessio_logout():
    """Logout user by destroying sessio"""
    from api.v1.app import auth
    if not auth.destroy_session(reques):
        abort(400)
    return jsonify({}), 200
