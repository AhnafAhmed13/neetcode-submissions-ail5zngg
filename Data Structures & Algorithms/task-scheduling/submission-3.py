class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import Counter
        # import heapq
        # count = Counter(tasks)

        # max_heap = [count[i] for i in count]
        # heapq.heapify_max(max_heap)

        # return (n * heapq.heappop_max(max_heap))

        counts = Counter(tasks).values()
        max_f = max(counts)
        n_max_f = list(counts).count(max_f)

        res = (max_f - 1) * (n + 1) + n_max_f
        return max(res, len(tasks))