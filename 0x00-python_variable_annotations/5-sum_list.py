#!/usr/bin/env python3
"""
a module which contains a function as described by the function
"""


def sum_list(input_list: list[float]) -> float:
    """takes a list of floats and returns their sum"""
    result = 0.0
    for num in input_list:
        result += num
    return result