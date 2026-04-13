class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        if len(sc) != len(tc):
            return False
        sf = sorted(list(sc.items()), key=lambda x: (x[1], x[0]))
        tf = sorted(list(tc.items()), key=lambda x: (x[1], x[0]))
        for i in range(len(sf)):
            if sf[i][1] != tf[i][1] or (sf[i][1] == tf[i][1] and sf[i][0] == tf[i][0]):
                return False
        return True