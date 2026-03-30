class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if len(nums) == 1 and nums[0] >= target:
            return 1

        min_len = len(nums) + 1
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                min_len = min(min_len, R - L + 1)
                curr_sum -= nums[L]
                L += 1
            
        return min_len if min_len <= len(nums) else 0

        