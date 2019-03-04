#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):

    input_list.sort()
    start = 0
    end = len(input_list) - 1
    if len(input_list) == 0:
        return None
    while start != end:
        cur = input_list[start] + input_list[end]
        if cur < n:
            start += 1
        elif cur > n:
            end -= 1
        else:
            an = (start, end)
            return an
    return None
