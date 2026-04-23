class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        row = 0
        while n >= i:
            n -= i
            i += 1
            row += 1
        return row
