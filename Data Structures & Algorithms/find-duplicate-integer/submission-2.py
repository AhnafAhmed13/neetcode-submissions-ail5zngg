class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = nums[0]
        while True:
            n = nums[i]
            if n == i: return n
            nums[i] = i
            i = n
