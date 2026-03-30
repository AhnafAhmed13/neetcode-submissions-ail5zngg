class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)[2:]
        res = "0" * (32 - len(res)) + res
        res = res[::-1]
        res = int(res, 2)
        return res