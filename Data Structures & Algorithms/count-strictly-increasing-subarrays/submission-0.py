class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = 1
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                res += (n * (n + 1) // 2)
                n = 1
            else: n += 1
        return res + (n * (n + 1) // 2)
