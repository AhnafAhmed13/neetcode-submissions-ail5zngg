class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq, math
        heapq.heapify_max(gifts)
        for _ in range(k):
            curr = heapq.heappop_max(gifts)
            curr = math.isqrt(curr)
            heapq.heappush_max(gifts, curr)
        return sum(gifts)