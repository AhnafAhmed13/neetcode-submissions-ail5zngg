class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        i = nums[0]
        nums = set(nums)
        while k > 0:
            i += 1
            if i not in nums:
                k -= 1
        return i