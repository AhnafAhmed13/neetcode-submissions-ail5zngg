class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for ch in s[1:]:
            if ch == "1": ones += 1
        zeros = 0
        if s[0] == "0": zeros += 1
        res = zeros + ones
        for ch in s[1:len(s) - 1]:
            if ch == "0":
                zeros += 1
            else:
                ones -= 1
            res = max(res, zeros + ones)
        return res