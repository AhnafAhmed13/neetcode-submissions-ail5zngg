class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        a = arrays[0][0]
        b = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - a, b - arrays[i][0])
            a = min(a, arrays[i][0])
            b = max(b, arrays[i][-1])
        return res