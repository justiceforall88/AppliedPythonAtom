#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    cir_count = 0
    sqr_count = 0
    fig_count = 0
    for s in input_string:
        if s == '(':
            cir_count += 1
        if s == ')':
            cir_count -= 1
        if cir_count < 0:
            return False
        if s == '[':
            sqr_count += 1
        if s == ']':
            sqr_count -= 1
        if sqr_count < 0:
            return False
        if s == '{':
            fig_count += 1
        if s == '}':
            fig_count -= 1
        if fig_count < 0:
            return False
    if cir_count == 0 and sqr_count == 0 and fig_count == 0:
        print(input_string)
        return True
    else:
        return False
