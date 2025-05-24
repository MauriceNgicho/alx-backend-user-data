#!/usr/bin/env python3
"""Module for filtering PII from log messages"""


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
