#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    tmp = {}
    for i in range(len(input_list)):
        if n - input_list[i] in tmp.values():
            for key in tmp.keys():
                if tmp[key] == n - input_list[i]:
                    return key, i
        else:
            tmp[i] = input_list[i]
    return None
