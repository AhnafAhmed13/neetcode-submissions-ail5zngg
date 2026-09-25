class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = { ch : i for i, ch in enumerate(keyboard)}
        res = pos[word[0]]
        for i in range(1, len(word)):
            res += abs(pos[word[i - 1]] - pos[word[i]])
        return res