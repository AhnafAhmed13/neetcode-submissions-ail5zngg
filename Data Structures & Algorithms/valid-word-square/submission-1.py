class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = [[] for _ in range(len(words[0]))]
        for c in range(len(words[0])):
            for r in range(len(words)):
                if c < len(words[r]):
                    cols[c].append(words[r][c])
        for i, row in enumerate(words):
            if row != ''.join(cols[i]):
                return False
        return True