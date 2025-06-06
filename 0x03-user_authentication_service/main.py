#!/usr/bin/env python3
"""Main test module to validate user authentication service"""

import requests

BASE_URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """Register a new user"""
    response = requests.post(f'{BASE_URL}/users', data={'email': email, 'password': password})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Try logging in with incorrect password"""
    response = requests.post(f'{BASE_URL}/sessions', data={'email': email, 'password': password})
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def log_in(email: str, password: str) -> str:
    """Log in a user with correct credentials"""
    response = requests.post(f'{BASE_URL}/sessions', data={'email': email, 'password': password})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "session_id" in response.cookies, "Missing session_id cookie"
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Try accessing profile without login"""
    response = requests.get(f'{BASE_URL}/profile')
    assert response.status_code == 403, f"Expected 403, got {response.status_code}"


def profile_logged(session_id: str) -> None:
    """Access profile with valid session"""
    cookies = {'session_id': session_id}
    response = requests.get(f'{BASE_URL}/profile', cookies=cookies)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "email" in response.json(), "Expected 'email' in response"


def log_out(session_id: str) -> None:
    """Log out the user"""
    cookies = {'session_id': session_id}
    response = requests.delete(f'{BASE_URL}/sessions', cookies=cookies)
    assert response.status_code == 302, f"Expected 302, got {response.status_code}"


def reset_password_token(email: str) -> str:
    """Request a password reset token"""
    response = requests.post(f'{BASE_URL}/reset_password', data={'email': email})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json = response.json()
    assert "reset_token" in json, "Missing reset_token"
    return json["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password using the reset token"""
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.put(f'{BASE_URL}/reset_password', data=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == {"email": email, "message": "Password updated"}


# Test sequence
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
