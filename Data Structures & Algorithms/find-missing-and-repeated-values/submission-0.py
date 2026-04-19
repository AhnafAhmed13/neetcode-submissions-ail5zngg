class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = None
        # nums = set([i for i in range(1, len(grid)**2 + 1)])
        nums = set()
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                val = grid[r][c]
                if val in nums:
                    a = val
                nums.add(val)
                total += val

        n = len(grid)
        expected = (n**2 * (n**2 + 1)) // 2
        b = expected - total + a
        return [a, b]
