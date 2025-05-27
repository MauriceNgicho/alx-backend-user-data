#!/usr/bin/env python3
"""Auth module to manage API authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False"""
        return (False)

    def authorization_header(self, request=None) -> List[str]:
        """Returns None"""
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return (None)
