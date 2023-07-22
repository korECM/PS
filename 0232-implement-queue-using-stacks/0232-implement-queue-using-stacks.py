class MyQueue:
    a_stack: list[int]
    b_stack: list[int]

    def __init__(self):
        self.a_stack = []
        self.b_stack = []

    def push(self, x: int) -> None:
        self.a_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.b_stack.pop()

    def peek(self) -> int:
        if not self.b_stack:
            while self.a_stack:
                self.b_stack.append(self.a_stack.pop())
        return self.b_stack[-1]

    def empty(self) -> bool:
        return self.a_stack == [] and self.b_stack == []
