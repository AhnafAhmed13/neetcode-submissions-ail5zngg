class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        candidates = set(mat[0])
        for row in mat[1:]:
            candidates &= set(row)
        if len(candidates) > 0:
            return sorted(list(candidates))[0]
        return -1
