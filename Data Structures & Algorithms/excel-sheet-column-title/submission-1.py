class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        A = ord("A")
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            curr = columnNumber % 26
            res = chr(A + curr) + res
            columnNumber //= 26
        return res