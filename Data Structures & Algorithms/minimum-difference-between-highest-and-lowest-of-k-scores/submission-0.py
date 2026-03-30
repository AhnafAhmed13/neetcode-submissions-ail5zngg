class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[k - 1] - nums[0]
        for i in range(1, len(nums) - k + 1):
            res = min(res, nums[k - 1 + i] - nums[i])
        return res