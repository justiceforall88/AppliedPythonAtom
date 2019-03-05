#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    mn = 1
    if n < 0:
        mn = -1
    n *= mn
    s = str(n)
    s_inv = s[::-1]
    n_inv = int(s_inv)
    return n_inv * mn
