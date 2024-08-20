#!/usr/bin/env python3
"""A coroutine called async_generation that takes no args"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Returns the async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
