class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = sorted(list(Counter(nums).items()), key=lambda x: (x[1], -x[0]))
        res = []
        for x, n in count:
            res.extend([x] * n)
        return res