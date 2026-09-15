class MovingAverage:
    from collections import deque
    def __init__(self, size: int):
        self.array = deque([])
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.array) == self.size:
            left = self.array.popleft()
            self.sum -= left
        self.array.append(val)
        self.sum += val
        return self.sum / len(self.array)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
