#!/usr/bin/env python3
"""Type-annotated funct which takes a list of floats as arg"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return their sum as a float"""
    return sum(input_list)
