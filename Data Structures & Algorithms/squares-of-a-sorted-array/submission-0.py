class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])
        # n = 0
        # for i in range(len(nums)):
        #     if nums[n] < 0:
        #         if nums[i] >= 0 and nums[i] < abs(nums[n]):
        #             nums[i], nums[n] = nums[n], nums[i]
        #             n += 1
        
