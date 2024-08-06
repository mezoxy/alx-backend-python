#!/usr/bin/env python3
''' 0-async_generator '''


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, int]:
    '''
        async_generator: An async generator that yields random float values.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
