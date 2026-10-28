class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return int(sum([int(d) for d in str(min(nums))]) % 2 == 0)
