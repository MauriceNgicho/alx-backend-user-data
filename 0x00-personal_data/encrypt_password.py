#!/usr/bin/env python3
"""
Module for password hashing
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly-generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Generate salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

