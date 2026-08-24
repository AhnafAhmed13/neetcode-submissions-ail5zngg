class Solution:
    import copy
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix); m = len(matrix[0])
        T = [[0] * n for _ in range(m)]
        for r in range(n):
            for c in range(m):
                T[c][r] = matrix[r][c]
        return T

#   rc 0 1 2
#   0 [1,0,5],
#   1 [2,4,3]

#   rc 0 1
#   0 [1,2],
#   1 [0,4],
#   2 [5,3]
