#!/usr/bin/env python3
''' 7-to_vk.py'''


from typing import Callable
import random


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        to_kv: Takes a str k and an int OR float v as args and returns a tuple
        Args:
            k: A string
            v: An integer or a float
            Return: A tuple (str, float)
    '''
    return lambda x: x * random.random()
