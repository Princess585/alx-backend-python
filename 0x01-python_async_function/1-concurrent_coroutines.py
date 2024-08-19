#!/usr/bin/ env python3
"""import wait_random from the previous python file"""
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all delays"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)
    
    return sorted_delays
