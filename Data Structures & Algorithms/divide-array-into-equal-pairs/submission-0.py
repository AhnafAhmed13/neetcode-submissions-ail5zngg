class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for num, freq in c.items():
            if freq % 2 != 0:
                return False
        return len(c) > 0