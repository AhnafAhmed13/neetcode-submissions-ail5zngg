class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        if n < 3:
            return trib[n]
        n -= 2
        while n > 0:
            next = sum(trib)
            trib = [trib[1], trib[2], next]
            n -= 1
        return trib[2]