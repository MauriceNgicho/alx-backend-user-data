#!/usr/bin/env python3
"""Module for filtering PII from log messages"""


import logging
import re
from typing import List
import os
import mysql.connector


# Constants
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str
        ) -> str:
    """Function for filtering the data"""
    return re.sub(
            rf'({"|".join(fields)})=.*?(?={separator})',
            lambda m: f'{m.group(1)}={redaction}', message
            )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class for logging sensitive information """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters sensitive fields using filter_datum"""
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.getMessage(),
                self.SEPARATOR
                )
        return super().format(record)


def get_logger() -> logging.Logger:
    """Create a logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RadactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """Returns a connection to the MySQL database using env variables."""
    username: str = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password: str = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host: str = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name: str = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
    )

def main() -> None:
    """
    Retrieves all rows in the users table and logs each row,
    redacting PII fields.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        message = "; ".join(f"{field}={value}" for field, value in zip(field_names, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
