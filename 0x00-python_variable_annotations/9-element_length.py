#!/usr/bin/env python3
from typing import List, Tuple
"""
a module containing the special function
"""


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """special decorations"""
    return [(i, len(i)) for i in lst]
