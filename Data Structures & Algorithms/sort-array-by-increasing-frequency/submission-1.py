class Solution:
    from collections import Counter
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))