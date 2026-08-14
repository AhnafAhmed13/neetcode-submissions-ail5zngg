class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1,2]
        for i in range(2,n):
            curr = dp[-1] + dp[-2]
            dp.append(curr)
        return dp[-1]
    