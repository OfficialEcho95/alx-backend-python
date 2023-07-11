#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
__import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """coroutine that will execute async_comprehension four times"""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
