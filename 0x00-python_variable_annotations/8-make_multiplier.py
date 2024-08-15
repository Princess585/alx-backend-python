#!/usr/bin/env python3
"""Function that make_multiplier take a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies"""

    def mult(m: float) -> float:
        """Returns a function that multiplies"""
        return m * multiplier

    return mult
