#!/usr/bin/env python3
"""Code with correct duck-typed annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns None"""
    if lst:
        return lst[0]
    else:
        return None
