class Solution:
    from collections import Counter
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1: return False
        sc = Counter(s)
        tc = Counter(t)
        chs = set(sc.keys()) | set(tc.keys())
        diff = 0
        for ch in chs:
            diff += abs(sc.get(ch, 0) - tc.get(ch, 0))
        return 1 <= diff <= 2