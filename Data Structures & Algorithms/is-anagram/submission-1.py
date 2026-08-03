class Solution:

    from collections import Counter

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)

        if len(count_s) != len(count_t):
            return False

        for ch in count_s:
            if ch not in t or count_s[ch] != count_t[ch]:
                return False

        return True