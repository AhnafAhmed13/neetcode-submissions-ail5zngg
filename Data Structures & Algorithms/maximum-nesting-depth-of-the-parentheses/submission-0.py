class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        lvl = 0
        for ch in s:
            if ch == "(":
                lvl += 1
                res = max(res, lvl)
            if ch == ")":
                lvl -= 1
        return res