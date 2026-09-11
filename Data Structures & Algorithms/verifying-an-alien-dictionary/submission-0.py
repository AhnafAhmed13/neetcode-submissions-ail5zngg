class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = { order[i] : chr(ord("a") + i) for i in range(len(order))}
        for i in range(len(words)):
            v = ""
            for c in words[i]:
                v += d[c]
            words[i] = v
        sorted_words = sorted(words)
        for i in range(len(words)):
            if sorted_words[i] != words[i]:
                return False
        return True