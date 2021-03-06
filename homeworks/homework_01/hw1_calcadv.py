#!/usr/bin/env python
# coding: utf-8
import pickle
ops = {'+': 1, '-': 1, '*': 2, '/': 2}


def is_correct(input_string):
    if not input_string:
        return None
    valid_char = "1234567890.+-*/() \t"
    digits = "1234567890."
    tmp = []
    num = ""
    br = 0
    is_operands = False
    for s in input_string:
        if s not in valid_char or br < 0:
            return False
        if s in digits:
            num += s
            is_operands = True
        elif num:
            tmp.append(1)
            num = ""
        if s in ops.keys() or s in "()":
            if s not in "()":
                if tmp:
                    if tmp[-1] == 0 and ops[s] == 2:
                        return False
                elif not tmp and ops[s] == 2:
                    return False
                tmp.append(0)
            else:
                if s == '(':
                    br += 1
                else:
                    br -= 1
    if num:
        tmp.append(1)
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i + 1] == 1:
            return False
    for s in range(len(input_string) - 1):
        if input_string[s] == '(' and input_string[s + 1] == ')':
            return False
    if br != 0 or not is_operands:
        return False
    return True


def _eval():
    def parsing(input_string):
        digits = "1234567890."
        tokens = []
        num = ""
        for s in input_string:
            if s in digits:
                num += s
            elif num:
                tokens.append(float(num))
                num = ""
            if s in ops.keys() or s in "()":
                tokens.append(s)
        if num:
            tokens.append(float(num))
        return tokens

    def to_reverse_polish(tokens):
        if not tokens:
            return None
        stack = []
        new_tokens = []
        for t in tokens:
            if t in ops.keys():
                while stack and stack[-1] != "(" and ops[t] <= ops[stack[-1]]:
                    new_tokens.append(stack.pop())
                stack.append(t)
            elif t == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    new_tokens.append(x)
            elif t == "(":
                stack.append(t)
            else:
                new_tokens.append(t)
        while stack:
            new_tokens.append(stack.pop())
        return new_tokens

    def calculate(tokens):
        if not tokens:
            return None
        stack = []
        for t in tokens:
            if t in ops.keys():
                y, x = stack.pop(), stack.pop()
                if t == '+':
                    res = x + y
                elif t == '-':
                    res = x - y
                elif t == '*':
                    res = x * y
                else:
                    if y != 0:
                        res = x / y
                    else:
                        return None
                stack.append(res)
            else:
                stack.append(t)
        return stack[0]

    return calculate(to_reverse_polish(parsing(input_string)))


def advanced_calculator(input_string):
    if not is_correct(input_string):
        return None
    return eval(input_string)
