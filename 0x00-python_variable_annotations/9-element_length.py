#!/usr/bin/env python3
"""unction’s parameters and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """special decorations"""
    return [(i, len(i)) for i in lst]
