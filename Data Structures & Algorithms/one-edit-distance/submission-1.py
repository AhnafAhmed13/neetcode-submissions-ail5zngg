class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        chs = set(sc.keys()) | set(tc.keys())
        diff = 0
        for ch in chs:
            diff += abs(sc.get(ch, 0) - tc.get(ch, 0))
        return diff == 1 or diff == 2