#!/usr/bin/env python3
"""
a module that imports task 0
"""
import asyncio
import heapq
from 0-basic_async_syntax.py import wait_random


async def wait_n(n: int, max_delay: float) -> list[float]:
    """a function that takes 2 int variables"""
    delays = []
    tasks = []

    # Spawn wait_random n times
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Await all the tasks and collect the delays
    for task in tasks:
        delay = await task
        heapq.heappush(delays, delay)

    # Extract the minimum elements from the heap
    sorted_delays = []
    while delays:
        sorted_delays.append(heapq.heappop(delays))

    return sorted_delays
