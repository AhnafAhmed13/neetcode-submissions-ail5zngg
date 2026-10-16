class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        count = len(matrix) * len(matrix[0])
        left = top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        res = []

        while left <= right and top <= bottom and len(res) < count:

            # row vector
            if top == bottom:
                res.extend(matrix[top][left:right+1])
                break

            # col vector
            elif left == right:
                res.extend([matrix[r][left] for r in range(top, bottom + 1)])
                break

            else:
                # left to right
                res.extend(matrix[top][left:right])

                # top to bottom
                for r in range(top, bottom + 1):
                    res.append(matrix[r][right])

                # right to left
                res.extend(matrix[bottom][left+1:right][::-1])

                # bottom to top
                for r in range(bottom, top, -1):
                    res.append(matrix[r][left])
                
                left += 1
                right -= 1
                top += 1
                bottom -= 1

        return res
