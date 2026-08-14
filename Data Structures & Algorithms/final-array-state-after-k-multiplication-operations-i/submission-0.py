class Solution:
    from collections import heapq
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            min, idx = heapq.heappop(heap)
            min *= multiplier
            heapq.heappush(heap, (min, idx))
        res = [n for n, _ in sorted(heap, key=lambda x: x[1])]
        return res
        