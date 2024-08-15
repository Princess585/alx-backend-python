#!/usr/bin/env python3
"""Function which takes a list of int and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return their sum as a float"""
    return sum(mxd_lst)
