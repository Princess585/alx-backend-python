#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new func"""
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]  
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
