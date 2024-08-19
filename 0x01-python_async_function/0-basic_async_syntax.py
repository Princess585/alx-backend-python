#!/usr/bin/env python3
"""Asynchronous coroutine that takes an an aint arg"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Raturns max delay include and float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
