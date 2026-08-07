class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if len(s) > len(t):
            return False

        pt, ps = 0, 0
        while pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                if ps == len(s):
                    return True
            pt += 1

        return False