class Solution:
    from collections import Counter
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        res = 0
        for w in words:
            wc = Counter(w)
            for ch in wc:
                if ch not in c or wc[ch] > c[ch]: break
            else: res += len(w)
        return res
