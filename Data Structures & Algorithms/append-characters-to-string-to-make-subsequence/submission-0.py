class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(s):
            if s[i] == t[j]:
                j += 1
                if j == len(t):
                    return 0
            i += 1
        return len(t) - j