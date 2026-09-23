class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sc = Counter(s); tc = Counter(t)
        if len(sc) != len(tc): return False
        for ch in sc:
            if ch not in tc: return False
            if sc[ch] != tc[ch]: return False
        for ch in tc:
            if ch not in sc: return False
            if tc[ch] != sc[ch]: return False
        return True