class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        digits = []
        while x > 0:
            digits.append(x % 10); x //= 10
        l = 0; r = len(digits) - 1
        while l < r:
            if digits[l] != digits[r]: return False
            l += 1; r -= 1
        return True
        