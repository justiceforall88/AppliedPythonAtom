#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):

    start = 0
    end = len(input_string) - 1
    while start < end:
        while not input_string[start].isalnum():
            start += 1
        while not input_string[end].isalnum():
            end -= 1
        if input_string[start].lower() != input_string[end].lower():
            return False
    return True
