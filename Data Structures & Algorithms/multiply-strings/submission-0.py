class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        factor = 1
        n1 = 0
        for i in range(len(num1) - 1, -1, -1):
            n = ord(num1[i]) - ord("0")
            n1 += (n * factor)
            factor *= 10
        factor = 1
        n2 = 0
        for i in range(len(num2) - 1, -1, -1):
            n = ord(num2[i]) - ord("0")
            n2 += (n * factor)
            factor *= 10
        prod = n1 * n2
        return str(prod)