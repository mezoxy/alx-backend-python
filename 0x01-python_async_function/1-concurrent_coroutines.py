#!/usr/bin/env python3
''' 1-concurrent_coroutines '''


import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''
        wait_n: Returns a list of delays

        Args:
            max_delay: An integer the maximum delay
            n: number of repate

        Return: A list of delays
    '''
    return await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
