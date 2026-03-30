class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n - 1

        while l <= r:

            mid = (l + r) // 2

            row, col = mid // n, mid % n
            # print(l, r, mid, row, col, matrix[row][col])
            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                r = mid - 1

            if matrix[row][col] < target:
                l = mid + 1

        return False