import sys
from collections import defaultdict
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

class NewArray:
    data: list[str]
    front_index: int
    back_index: int
    is_reversed: bool

    def __init__(self, data: list[str]):
        self.data = data
        self.is_reversed = False
        self.front_index = 0
        self.back_index = len(data)

    def reverse(self):
        self.is_reversed = not self.is_reversed

    def pop(self):
        if self.is_reversed:
            self.back_index -= 1
        else:
            self.front_index += 1

    def get_data(self):
        direct_ = self.data[self.front_index:self.back_index] \
            if not self.is_reversed \
            else self.data[self.back_index - 1:None if self.front_index == 0 else self.front_index - 1:-1]
        return f"[{','.join(direct_)}]"


t = num_input()
for _ in range(t):
    func = input()
    n = num_input()
    raw_input = input()[1:-1].replace("RR", "")
    array = NewArray(list(raw_input.split(',')) if n > 0 else [])
    if func.count("D") > n:
        print("error")
        continue
    for f in func:
        if f == "R":
            array.reverse()
        else:
            array.pop()
    print(array.get_data())
