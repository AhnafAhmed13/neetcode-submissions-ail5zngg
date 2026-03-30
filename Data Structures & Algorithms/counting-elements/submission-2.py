class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter
        count = Counter(arr)
        res = 0
        for n in set(arr):
            if n + 1 in count:
                res += count[n]
        return res