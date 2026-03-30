class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = {k: i for i, k in enumerate(keyboard)}
        res = keyboard[word[0]]
        for i in range(len(word) - 1):
            res += abs(keyboard[word[i]] - keyboard[word[i + 1]])
        return res