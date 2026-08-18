class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        for k, v in ct.items():
            if k not in cs or cs[k] < v:
                return  k