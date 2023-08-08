import sys
from collections import deque

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

class NewArray:
    data: deque[int]
    is_reversed: bool

    def __init__(self, data: list[int]):
        self.data = deque(data)
        self.is_reversed = False

    def reverse(self):
        self.is_reversed = not self.is_reversed

    def pop(self):
        if self.is_reversed:
            self.data.pop()
        else:
            self.data.popleft()

    def get_data(self):
        target = reversed(self.data) if self.is_reversed else self.data
        return f"[{','.join(map(str, target))}]"


t = num_input()
for _ in range(t):
    func = input()
    n = num_input()
    raw_input = input()[1:-1]
    array = NewArray(list(map(int, raw_input.split(','))) if n > 0 else [])
    if func.count("D") > n:
        print("error")
        continue
    for f in func:
        if f == "R":
            array.reverse()
        else:
            array.pop()
    print(array.get_data())
