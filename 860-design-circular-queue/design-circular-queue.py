class MyCircularQueue:
    # ring buffer
    def __init__(self, k: int):
        self.k = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0
    # enQueue(): move rear pointer
    def enQueue(self, value: int) -> bool:
        if self.k[self.rear] is None:
            self.k[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False
    # deQueue(): move front pointer
    def deQueue(self) -> bool:
        if self.k[self.front] is None:
            return False
        else:
            self.k[self.front] = None
            self.front = (self.front + 1) % self.maxlen 
            # %: 포인터의 위치가 전체 길이를 벗어나지 않도록
            return True      

    def Front(self) -> int:
        return -1 if self.k[self.front] is None else self.k[self.front]

    def Rear(self) -> int:
        return -1 if self.k[self.rear - 1] is None else self.k[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.k[self.front] is None
    # rear와 front가 만나게 되면 full
    def isFull(self) -> bool:
        return self.front == self.rear and self.k[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()