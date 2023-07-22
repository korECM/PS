from collections import deque


class MyStack:
    main_queue: deque[int]

    def __init__(self):
        self.main_queue = deque()

    def push(self, x: int) -> None:
        self.main_queue.appendleft(x)
        for _ in range(len(self.main_queue) - 1):
            self.main_queue.appendleft(self.main_queue.pop())

    def pop(self) -> int:
        return self.main_queue.pop()

    def top(self) -> int:
        return self.main_queue[-1]

    def empty(self) -> bool:
        return len(self.main_queue) == 0
