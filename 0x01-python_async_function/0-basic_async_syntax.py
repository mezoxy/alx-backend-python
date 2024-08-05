#!/usr/bin/env python3
''' 0-basic_async_syntax '''


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
        wait_random: takes in an integer that waits for a random delay

        Args:
            max_delay: An integer

        Return: A float
    '''
    delay = random.random() * max_delay
    await asyncio.sleep(int(delay))

    return delay
