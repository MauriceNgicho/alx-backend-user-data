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
