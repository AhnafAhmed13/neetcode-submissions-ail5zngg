class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        alls = set([n for n in range(len(nums) + 1)])
        return (alls - set(nums)).pop()