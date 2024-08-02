#!/usr/bin/env python3
''' 7-to_vk.py'''


from typing import Callable


def fun(n: float) -> float:
    return n * 1.1


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        to_kv: Takes a str k and an int OR float v as args and returns a tuple
        Args:
            k: A string
            v: An integer or a float
            Return: A tuple (str, float)
    '''
    return fun
