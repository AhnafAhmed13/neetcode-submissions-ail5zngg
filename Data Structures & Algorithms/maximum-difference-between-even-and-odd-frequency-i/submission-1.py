class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        freqs = sorted(list(count.values()))
        max_even, max_odd, min_even, min_odd = float('-inf'), float('-inf'), float('inf'), float('inf')
        for f in freqs:
            if f % 2 == 0:
                max_even = max(max_even, f)
                min_even = min(min_even, f)
            else:
                max_odd = max(max_odd, f)
                min_odd = min(min_odd, f)
        return max((min_odd - max_even), (max_odd - min_even))
