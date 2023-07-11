#!/usr/bin/env python3
"""
module holds function which yields a rand number
"""

import asyncio
import random
from 0 - async_generator.py import async_generator


async def async_comprehension():
    """
    coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers
    """
    return [i async for i in async_generator()]