class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            curr = nums[l] + nums[r]
            if curr < k:
                res = max(res, curr)
                l += 1
            else:
                r -= 1
        return res