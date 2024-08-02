#!/usr/bin/env python3
''' 9-element_length.py '''


from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        element_length: A function that returns a list of tuples
        Args:
            lst: An iterable obj
        Return: A list of tuples
    '''
    return [(i, len(i)) for i in lst]
