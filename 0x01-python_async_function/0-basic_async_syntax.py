#!/usr/bin/env python3
"""
A module that contains a funtion that takes a random
float, sleeps then return the float
"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """the function that receives the integer and passes it"""
    r = random.uniform(0, max_delay)

    await asyncio.sleep(r)
    return r
