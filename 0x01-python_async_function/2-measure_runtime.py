#!/usr/bin/env python3
''' 1-concurrent_coroutines '''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        measure_time: Measures the total execution time for wait_n

        Args:
            max_delay: An integer the maximum delay
            n: number of repate

        Return: total_time / n
    '''
    lis = asyncio.run(wait_n(n, max_delay))

    return sum(lis) / n
