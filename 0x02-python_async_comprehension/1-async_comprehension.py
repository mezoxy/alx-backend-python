#!/usr/bin/env python3
'''1-async_comprehension.py'''


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        async_comprehension: A corotine that collect 10 random float
        Return: 10 random numbers
    '''
    return [i async for i in async_generator()]
