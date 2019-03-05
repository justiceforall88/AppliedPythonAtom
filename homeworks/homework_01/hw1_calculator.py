#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    x_c = isinstance(x, int) or isinstance(x, float) or isinstance(x, complex)
    y_c = isinstance(y, int) or isinstance(y, float) or isinstance(y, complex)
    if not (x_c and y_c):
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
