#!/usr/bin/env python3
''' 0-async_generator '''


import asyncio
import random


async def async_generator():
    '''
        async_generator: An async generator
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
