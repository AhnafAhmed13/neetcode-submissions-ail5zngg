class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = {}
        res = -1
        for i, c in enumerate(s):
            if c in idx:
                res = max(res, i - idx[c] - 1)
            else:
                idx[c] = i
        return res