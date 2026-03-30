class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        res = 0
        for v in c.values():
            if v > 1:
                res += sum(range(1,v))
        return res
