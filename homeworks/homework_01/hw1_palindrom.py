#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):

    start = 0
    end = len(input_string) - 1
    if len(input_string) == 0:
        return True
    while start < end:
        print(start, end)
        while not input_string[start].isalnum():
            start += 1
            if start == end:
                return True
        while not input_string[end].isalnum():
            end -= 1
            if start == end:
                return True
        if input_string[start].lower() != input_string[end].lower():
            return False
        start += 1
        end -= 1
    return True
