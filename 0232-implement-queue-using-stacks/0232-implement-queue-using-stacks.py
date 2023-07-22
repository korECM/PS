class MyQueue:
    a_stack: list[int]
    b_stack: list[int]

    def __init__(self):
        self.a_stack = []
        self.b_stack = []

    def push(self, x: int) -> None:
        self.a_stack.append(x)

    def pop(self) -> int:
        if self.b_stack:
            return self.b_stack.pop()
        for _ in range(len(self.a_stack)):
            self.b_stack.append(self.a_stack.pop())
        return self.b_stack.pop()

    def peek(self) -> int:
        if self.b_stack:
            return self.b_stack[-1]
        for _ in range(len(self.a_stack)):
            self.b_stack.append(self.a_stack.pop())
        return self.b_stack[-1]

    def empty(self) -> bool:
        return len(self.a_stack) == 0 and len(self.b_stack) == 0
