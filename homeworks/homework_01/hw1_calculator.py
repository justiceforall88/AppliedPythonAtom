#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    x_cond = isinstance(x, int) | isinstance(x, float) | isinstance(x, complex)
    y_cond = isinstance(y, int) | isinstance(y, float) | isinstance(y, complex)
    if not (x_cond & y_cond):
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


