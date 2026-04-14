class Solution:
    def check(self, nums: List[int]) -> bool:
        rot = True if nums[-1] > nums[0] else False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if rot:
                    return False
                rot = True
        return True