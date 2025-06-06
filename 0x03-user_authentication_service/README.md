 0x03 - User Authentication Service

Secure User Authentication Microservice in Flask

Project Overview

This project is a secure authentication microservice built with Python, Flask, and SQLAlchemy. It handles user registration, login, logout, profile access, and password reset functionality — all backed by robust session management and password hashing using bcrypt.

The project follows best practices in user authentication and is part of the ALX Backend specialization.

✅ Features Implemented

User Registration

POST /users

Securely registers a new user using a hashed password

User Login (Session-based)

POST /sessions

Validates user credentials and returns a session cookie

Profile Access

GET /profile

Retrieves user email using session ID from cookie

Logout

DELETE /sessions

Destroys the user session and logs them out

Password Reset Flow

POST /reset_password — generates a reset token

PUT /reset_password — resets the password using the token

Tech Stack

Layer

Tool

Backend Framework

Flask

Database

SQLite (via SQLAlchemy ORM)

Password Hashing

bcrypt

UUIDs

uuid for session and reset tokens

Project Structure

0x03-user_authentication_service/
│
├— app.py             # Flask routes
├— auth.py            # Core Auth class (business logic)
├— db.py              # SQLAlchemy ORM database interface
├— user.py            # SQLAlchemy User model
├— main.py            # Test runner
├— *.py               # Additional test scripts
├— a.db               # SQLite database
├— README.md          # This file
├— requirements.txt   # Python dependencies
└— __pycache__/       # Python bytecode (ignored)

Key Concepts Learned

Concept

Description

Password Hashing

Used bcrypt to securely store passwords.

Session Management

Generated and destroyed session IDs stored in cookies.

ORM (SQLAlchemy)

Queried and updated user data safely using SQLAlchemy.

Secure Routes

Restricted access using session validation.

Password Reset Flow

Implemented token-based reset functionality.

🧐 What I Learned

How to design a secure authentication system using Flask

The importance of not storing plaintext passwords

Proper session management and secure logout mechanisms

How to use SQLAlchemy to abstract low-level SQL operations

How to return appropriate HTTP status codes and messages

The value of clean separation between database, business logic, and routes

🧠 Reflections

Initially, I struggled with:

Understanding how bcrypt hashes and verifies passwords

Proper use of UUIDs for sessions and reset tokens

Returning the correct HTTP status codes (e.g., 302 vs 200)

Securely handling user input without exposing sensitive data

But by working through each task, testing thoroughly, and refactoring as needed, I gained solid confidence in backend authentication



🛠️ Run Locally

Clone this repository

git clone https://github.com/your-username/0x03-user_authentication_service.git
cd 0x03-user_authentication_service

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Flask server:
