class MyQueue:
    a_stack: list[int]
    b_stack: list[int]

    def __init__(self):
        self.a_stack = []
        self.b_stack = []

    def push(self, x: int) -> None:
        while self.a_stack:
            self.b_stack.append(self.a_stack.pop())
        self.a_stack.append(x)
        while self.b_stack:
            self.a_stack.append(self.b_stack.pop())

    def pop(self) -> int:
        return self.a_stack.pop()

    def peek(self) -> int:
        return self.a_stack[-1]

    def empty(self) -> bool:
        return len(self.a_stack) == 0