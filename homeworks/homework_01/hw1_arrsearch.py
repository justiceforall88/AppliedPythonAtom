#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    tmp = {}
    k = 0
    for a in input_list:
        if n - a in tmp.values():
            for key in tmp.keys():
                if tmp[key] == n - a:
                    return key, k
        else:
            tmp[k] = a
        k += 1
    return None
