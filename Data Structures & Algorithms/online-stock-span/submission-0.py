class StockSpanner:

    def __init__(self):
        self.history = []

    def next(self, price: int) -> int:
        self.history.append(price)
        if len(self.history) == 1:
            return 1
        i = len(self.history) - 1
        while i >= 0:
            if self.history[i] <= price:
                i -= 1
            else:
                return len(self.history) - i - 1
        return len(self.history)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)