#!/usr/bin/env python3
''' 0-async_generator '''


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> Generator[float, None, None]:
    '''
        async_generator: An async generator that yields random float values.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
