#!/usr/bin/env python3
"""Auth module to manage API authentication"""


from flask import request
from typing import List, TypeVar
import os


class Auth:
    """A class to manage authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded == path:
                return False
        return True

    def authorization_header(self, request=None) -> List[str]:
        """Returns None"""
        if request is None:
            return (None)
        if 'Authorization' not in request.headers:
            return (None)
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return (None)

    def session_cookie(self, request=None):
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)

