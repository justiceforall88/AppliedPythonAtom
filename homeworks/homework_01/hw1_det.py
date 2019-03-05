#!/usr/bin/env python
# coding: utf-8


def minor(list_of_lists, i, j):
    for k in range(len(list_of_lists)):
        list_of_lists[k].pop(j)
    list_of_lists.pop(i)
    return list_of_lists

def calculate_determinant(list_of_lists):
    n = len(list_of_lists)
    if n == 0:
        return None
    for k in range(n):
        if len(list_of_lists[k]) != n:
            return None
    if n == 1:
        return list_of_lists[0][0]
    else:
        det = 0
        for k in range(n):
            det += ((-1)**k)*list_of_lists[0][k]*calculate_determinant(minor(list_of_lists, 0, k))
