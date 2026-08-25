class HitCounter:
    from collections import deque
    def __init__(self):
        self.counter = deque([])

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.counter) > 0 and self.counter[0] <= timestamp - 300:
            self.counter.popleft()
        return len(self.counter)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
