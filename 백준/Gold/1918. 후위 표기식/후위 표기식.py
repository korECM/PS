import sys
from collections import defaultdict
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

low_order = ['+', '-']
high_order = ['*', '/']
all_operator = low_order + high_order


def postfix(s: str):
    operands_stack, operator_stack = [], []

    def calc():
        a, b = operands_stack.pop(), operands_stack.pop()
        op = operator_stack.pop()
        operands_stack.append(f'{b}{a}{op}')

    index = 0
    while index < len(s):
        c = s[index]
        if c.isalpha():
            operands_stack.append(c)
        elif c == '(':
            left_count = 1
            index += 1
            start = index
            while left_count:
                if s[index] == '(':
                    left_count += 1
                elif s[index] == ')':
                    left_count -= 1
                index += 1
            index -= 1
            end = index
            operands_stack.append(postfix(s[start:end]))
        elif c in all_operator:
            while operator_stack and len(operands_stack) >= 2 and not (
                    c in high_order and operator_stack[-1] in low_order):
                calc()
            operator_stack.append(c)
        index += 1
    while operator_stack:
        calc()
    return operands_stack[0]


print(postfix(IO.input()))
