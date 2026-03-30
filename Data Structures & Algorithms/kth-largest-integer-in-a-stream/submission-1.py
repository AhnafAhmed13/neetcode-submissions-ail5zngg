import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify_max(self.nums)
        tmp = []
        for _ in range(self.k):
            tmp.append(heapq.heappop_max(self.nums))
        res = tmp[-1]
        while tmp:
            heapq.heappush_max(self.nums, tmp.pop())
        return res
