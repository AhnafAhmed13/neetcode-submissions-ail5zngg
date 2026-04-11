class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for c in range(len(words[0])):
            col = []
            for r in range(len(words)):
                if c < len(words[r]):
                    col.append(words[r][c])
            if words[c] != ''.join(col):
                return False
        return True