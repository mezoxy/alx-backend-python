#!/usr/bin/env python3
''' 6-sum_mixed_list.py'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''
        sum_list: Caclculate the sum of floats in an array
        Args:
            input_list: An array of floats
            Return: The sum of floats as a float
    '''
    return sum(mxd_lst)
