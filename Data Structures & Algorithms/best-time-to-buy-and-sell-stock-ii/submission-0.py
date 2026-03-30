class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += (prices[i] - prices[i - 1])
            # print(res, i - 1, prices[i - 1], i, prices[i])
        return res