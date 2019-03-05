#!/usr/bin/env python
# coding: utf-8


def splitvals(val, t):
    if isinstance(val, set) or isinstance(val, tuple) or isinstance(val, list):
        for i in val:
            splitvals(i, t)
    else:
        t.append(val)


def invert_dict(source_dict):
    tmp_dict = dict()
    new_dict = dict()
    print(source_dict)
    for k, v in source_dict.items():
        arr = []
        splitvals(v, arr)
        tmp_dict[k] = arr
    for k, v in tmp_dict.items():
        for el in v:
            if el not in new_dict.keys():
                new_dict[el] = k
            else:
                if not isinstance(new_dict[el], list):
                    new_dict[el] = [new_dict[el]]
                new_dict[el].append(i)
    return new_dict
