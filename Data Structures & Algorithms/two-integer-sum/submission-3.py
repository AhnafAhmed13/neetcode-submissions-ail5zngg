class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(x, i) for i, x in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        l = 0; r = len(nums) - 1
        while l < r:
            curr = nums[l][0] + nums[r][0]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return sorted([nums[l][1], nums[r][1]])