class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.window = []

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.sum += val
            return self.sum / len(self.window)
        else:
            self.window.append(val)
            self.sum += val
            self.sum -= self.window[len(self.window) - self.size - 1]
            return self.sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
