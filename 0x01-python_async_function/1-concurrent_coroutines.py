#!/usr/bin/env python3
''' 1-concurrent_coroutines '''


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        wait_n: Returns a list of delays

        Args:
            max_delay: An integer the maximum delay
            n: number of repate

        Return: A list of delays
    '''
    lis = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    lis1 = []
    for i in range(n):
        lis1.append(min(lis))
        lis.remove(min(lis))
    return lis1
