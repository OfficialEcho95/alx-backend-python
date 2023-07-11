#!/usr/bin/env python3
"""
module holds function which yields a rand number
"""

import asyncio
import random


async def async_generator():
    """function which takes no argument and returns the generated random"""
    i: int = 0
    while (i < 10):
        await asyncio.sleep(1)
        r = random.uniform(0, 10)
        yield r
        i += 1
