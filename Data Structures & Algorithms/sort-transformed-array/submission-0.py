class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = a * nums[i]**2 + b * nums[i] + c
        return sorted(nums)
