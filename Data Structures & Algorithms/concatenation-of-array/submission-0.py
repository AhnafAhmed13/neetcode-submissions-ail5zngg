class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = deepcopy(nums)
        ans += nums
        return ans
        