class Solution:
    from collections import Counter
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        res = []
        for n in arr2:
            res.extend([n] * counts[n])
            del counts[n]
        if counts:
            rest = []
            for n in counts:
                rest.extend([n] * counts[n])
            rest.sort()
        res.extend(rest)
        return res
        