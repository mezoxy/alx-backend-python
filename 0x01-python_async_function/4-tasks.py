#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
        task_wait_n
        Args:
            n: int
            max_delay: int
        Return: List of floats
    '''
    lis = await asyncio.gather(
            *[task_wait_random(max_delay) for _ in range(n)])
    return lis
