class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        res = 0
        balance = 0
        for t in transactions:
            if t >= 0: # received
                balance += t
                res += 1
            else: # sent
                if abs(t) <= balance:
                    balance -= abs(t)
                    res += 1
        return res