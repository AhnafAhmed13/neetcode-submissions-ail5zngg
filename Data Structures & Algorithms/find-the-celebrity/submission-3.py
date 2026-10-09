# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        db = [[None] * n for _ in range(n)]
        for a in range(n):
            for b in range(n): db[a][b] = knows(a, b)
        candidates = []
        # Find who doesn't know anyone
        for a in range(n):
            for b in range(n):
                if a != b and db[a][b]: break
            else: candidates.append(a)
        res = -1
        # Find whom everyone knows
        for candidate in candidates:
            for i in range(n):
                if not db[i][candidate]: break
            else:
                if res != -1: return -1
                else: res = candidate
        return res