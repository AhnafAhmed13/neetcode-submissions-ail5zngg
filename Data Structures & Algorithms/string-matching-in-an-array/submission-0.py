class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = set(words)
        res = []
        for w in words:
            s.remove(w)
            for v in s:
                if w in v:
                    res.append(w)
                    break
            s.add(w)
        return res