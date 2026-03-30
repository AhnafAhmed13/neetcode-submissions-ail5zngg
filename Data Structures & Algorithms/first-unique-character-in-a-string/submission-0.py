class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        idx = {}
        for i, ch in enumerate(s):
            if ch not in seen:
                idx[ch] = i
                seen.add(ch)
            else:
                if ch in idx:
                    del idx[ch]
        if len(idx) == 0:
            return -1
        uniques = list(idx.items())
        uniques.sort(key=lambda x: x[1])
        return uniques[0][1]
            