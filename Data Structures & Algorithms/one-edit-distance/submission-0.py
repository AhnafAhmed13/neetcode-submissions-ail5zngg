class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        print(sc)
        print(tc)
        diff = 0
        chs = set(sc.keys()) | set(tc.keys())
        for ch in chs:
            diff += abs(sc[ch] - tc.get(ch, 0))
        print(diff)
        return diff == 1 or diff == 2