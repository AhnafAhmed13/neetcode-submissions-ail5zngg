class Solution:
    from collections import Counter
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for v in counts.values():
            if v == 1:
                return -1
            res += math.ceil(v / 3)
        return res