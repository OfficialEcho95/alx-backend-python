#!/usr/bin/env python3
"""
a module of mixed function
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """takes int and dfloat and returns float"""
    return sum(mxd_lst)