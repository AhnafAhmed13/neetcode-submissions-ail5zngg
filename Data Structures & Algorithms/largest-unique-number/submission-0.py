class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import Counter
        nums.sort(reverse=True)
        count = Counter(nums)
        for n in nums:
            if count[n] == 1:
                return n
        return -1