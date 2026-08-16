class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low == high:
            return 1 if low % 2 == 1 else 0

        res = 0

        if low % 2 == 1:
            low += 1
            res += 1
        
        if high % 2 == 1:
            high -= 1
            res += 1

        res += (high - low) // 2

        return res