#!/usr/bin/env python3
''' 7-to_vk.py'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        make_multiplier: that takes a float multiplier as argument
        Args:
            multiplier: A float
        Return: A function that multiplies a float by multiplier
    '''
    return lambda x: x * multiplier
