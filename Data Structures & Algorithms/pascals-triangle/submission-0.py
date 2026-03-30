class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        for _ in range(2, numRows):
            curr = [1]
            for i in range(len(res[-1]) - 1):
                curr.append(res[-1][i] + res[-1][i + 1])
            curr.append(1)
            res.append(curr)
        return res
