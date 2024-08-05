#!/usr/bin/env python3
''' 1-concurrent_coroutines '''


import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    '''
        wait_n: Returns a list of delays

        Args:
            max_delay: An integer the maximum delay
            n: number of repate

        Return: A list of delays
    '''
    obj = asyncio.Task(wait_random(max_delay))

    return obj
