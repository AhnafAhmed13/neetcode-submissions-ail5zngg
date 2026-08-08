class Solution:
    def maxScore(self, s: str) -> int:
        zeroes, ones = [0], [0]
        for digit in s:
            if digit == '0':
                zeroes.append(zeroes[-1] + 1)
            else:
                zeroes.append(zeroes[-1])
        zeroes = zeroes[1:]
        
        for digit in s[::-1]:
            if digit == '1':
                ones.append(ones[-1] + 1)
            else:
                ones.append(ones[-1])

        ones = ones[1:][::-1]

        # if zeroes[-1] == 0:
        #     return ones[1]
        
        # if ones[0] == 0:
        #     return zeroes[-2]
        
        res = 0

        for i in range(len(zeroes) - 1):
            res = max(res, zeroes[i] + ones[i + 1])

        return res