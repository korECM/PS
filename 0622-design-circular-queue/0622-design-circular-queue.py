class MyCircularQueue:
    data: list[int]
    size: int
    head: int
    tail: int

    def __init__(self, k: int):
        self.data = [-1] * k
        self.size = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.head] = value
        self.head = (self.head + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.tail] = -1
        self.tail = (self.tail + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.head - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.data[self.head] == -1

    def isFull(self) -> bool:
        return self.head == self.tail and self.data[self.head] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
