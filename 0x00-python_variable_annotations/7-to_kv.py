#!/usr/bin/env python3
from typing import Union, Tuple
"""
a module containing the function described below
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that returns a tuple of str and float"""
    return k, float(v * v)
