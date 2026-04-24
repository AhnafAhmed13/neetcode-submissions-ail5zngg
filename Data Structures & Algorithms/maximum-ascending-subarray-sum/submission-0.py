class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += nums[i]
            else:
                res = max(res, curr)
                curr = nums[i]
        return max(res, curr)