class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        p = 0
        for i in range(len(t)):
            if p < len(s) and s[p] == t[i]:
                p += 1
            if p == len(s):
                return True
        
        return False