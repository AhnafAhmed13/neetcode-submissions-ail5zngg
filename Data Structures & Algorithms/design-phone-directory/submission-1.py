class PhoneDirectory:
    import heapq
    def __init__(self, maxNumbers: int):
        self.max_num = maxNumbers
        self.curr_num = 0
        self.directory = set()
        self.recycle_heap = []

    def get(self) -> int:
        if len(self.directory) == self.max_num: return -1
        if self.curr_num == self.max_num\
        and len(self.recycle_heap) == 0: return -1
        if len(self.recycle_heap) > 0:
            num = heapq.heappop(self.recycle_heap)
            self.directory.add(num)
            return num
        if self.curr_num < self.max_num:
            num = self.curr_num
            self.directory.add(self.curr_num)
            self.curr_num += 1
            return num
        return -1

    def check(self, number: int) -> bool:
        return number not in self.directory

    def release(self, number: int) -> None:
        if number in self.directory:
            self.directory.remove(number)
            heapq.heappush(self.recycle_heap, number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
