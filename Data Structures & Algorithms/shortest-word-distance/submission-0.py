class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        res = float('inf')
        for i, w in enumerate(wordsDict):
            if w == word1:
                w1 = i
                if w2 >= 0:
                    res = min(res, abs(w1 - w2))
            if w == word2:
                w2 = i
                if w1 >= 0:
                    res = min(res, abs(w1 - w2))
        return res
