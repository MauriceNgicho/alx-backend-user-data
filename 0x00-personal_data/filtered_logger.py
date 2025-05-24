#!/usr/bin/env python3
"""Module for filtering PII from log messages"""


import logging
import re
from typing import List


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
