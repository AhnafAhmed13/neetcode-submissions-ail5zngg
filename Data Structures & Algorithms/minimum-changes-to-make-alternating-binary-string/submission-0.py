class Solution:
    def minOperations(self, s: str) -> int:

        res0, res1 = 0, 0
        zero = True
        for bit in s:
            if zero:
                if bit == '1':
                    res0 += 1
                else:
                    res1 += 1
            else: # 1
                if bit == '0':
                    res0 += 1
                else:
                    res1 += 1
            zero ^= 1

        return min(res0, res1)