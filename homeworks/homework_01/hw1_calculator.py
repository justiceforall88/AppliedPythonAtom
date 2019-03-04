#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if not (isinstance(x, int) | isinstance(x, float) | isinstance(x, complex)) \
           & (isinstance(y, int) | isinstance(y, float) | isinstance(y, complex)):
        return None
    if operator == 'plus':
        return x + y
    elif operator == 'minus':
        return x - y
    elif operator == 'mult':
        return x * y
    elif operator == 'divide':
        if y != 0:
            return x / y
        else:
            return None
    else:
        return None


