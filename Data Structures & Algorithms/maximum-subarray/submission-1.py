class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]
        for i in range(1, len(nums)):
            if curr + nums[i] < nums[i]:
                curr = nums[i]
            else:
                curr += nums[i]
            res = max(res, curr)
        return res