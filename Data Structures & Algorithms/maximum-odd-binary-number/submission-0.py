class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones, zeroes = 0, 0
        for d in s:
            if d == '0':
                zeroes += 1
            else:
                ones += 1
        res = ['1'] * (ones - 1)
        res.extend(['0'] * zeroes)
        res.append('1')
        return ''.join(res)