from collections import deque


class MyStack:
    main_queue: deque[int]
    temp_queue: deque[int]

    def __init__(self):
        self.main_queue = deque()
        self.temp_queue = deque()

    def push(self, x: int) -> None:
        while self.main_queue:
            self.temp_queue.appendleft(self.main_queue.pop())
        self.main_queue.appendleft(x)
        while self.temp_queue:
            self.main_queue.appendleft(self.temp_queue.pop())

    def pop(self) -> int:
        return self.main_queue.pop()

    def top(self) -> int:
        element = self.pop()
        self.push(element)
        return element

    def empty(self) -> bool:
        print(self.main_queue)
        return len(self.main_queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
