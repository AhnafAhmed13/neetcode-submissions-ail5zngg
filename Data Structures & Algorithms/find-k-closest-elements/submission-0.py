class Solution:
    import heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for n in arr[:k]:
            y = abs(x - n)
            heap.append((-y, n))
        heapq.heapify(heap)
        for n in arr[k:]:
            y = abs(x - n)
            if -y > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-y, n))
        return sorted([n for _, n in heap])