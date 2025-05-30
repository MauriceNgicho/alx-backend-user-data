#!/usr/bin/env python3
"""SessionAuth module for session authentication"""


import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session-based authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """A method to create a session ID"""
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new unique session ID
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return user ID based on session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return a User instance based on a session cookie value"""
        if request is None:
            return None

        # Get session ID from cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get user ID from session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)
