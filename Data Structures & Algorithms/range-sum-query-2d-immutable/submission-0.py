class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prows = deepcopy(matrix)

        for row in range(m):
            for col in range(1, n):
                self.prows[row][col] = self.prows[row][col - 1] + matrix[row][col]
        
        self.pcols = deepcopy(self.prows)

        for col in range(n):
            for row in range(1, m):
                self.pcols[row][col] = self.pcols[row - 1][col] + self.prows[row][col]
        
        # print(self.prows)
        # print(self.pcols)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            if col1 == 0:
                return self.pcols[row2][col2]
            else: # col1 != 0
                return self.pcols[row2][col2] - self.pcols[row2][col1 - 1]
        else: # row1 != 0
            if col1 == 0:
                return self.pcols[row2][col2] - self.pcols[row1 - 1][col2]
            else: # col1 != 0
                return self.pcols[row2][col2] - self.pcols[row1 - 1][col2] - self.pcols[row2][col1 - 1] + self.pcols[row1 - 1][col1 - 1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)