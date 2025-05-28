#!/usr/bin/env python3
"""
BasicAuth module for Basic Authentication
"""


import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """Return Base64 part of Authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
