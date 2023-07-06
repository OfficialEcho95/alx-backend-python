#!/usr/bin/env python3
"""
a module of mixed function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float , int]]) -> float:
    """takes int and float and returns float"""
    return sum(mxd_lst)