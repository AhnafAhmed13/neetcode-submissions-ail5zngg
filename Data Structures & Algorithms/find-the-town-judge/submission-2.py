class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = set(); b = {}
        for i in range(len(trust)):
            a.add(trust[i][0])
            b[trust[i][1]] = 1 + b.get(trust[i][1], 0)
        for i in range(1, n + 1):
            if i not in a and i in b and b[i] == n - 1:
                return i
        return -1