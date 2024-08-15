#!/usr/bin/env python3
"""Function that takes a str and an int or float as arg"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v**2)
