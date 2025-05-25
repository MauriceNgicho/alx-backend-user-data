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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password to compare against.
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
