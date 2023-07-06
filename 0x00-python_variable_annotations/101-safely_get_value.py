#!/usr/bin/env python3
"""parameters and the return values, add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


<<<<<<< HEAD
def safely_get_value(dct: Mapping, key: Any, default:
                     Optional[T] = None) -> Union[Any, T]:
    """return dct"""
    if key in dct:
        return dct[key]
    else:
        return default
=======
def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list of integers multiplied by certain factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
>>>>>>> 2324db5f43d9aed292f4f2368e2ef4a881660085
