class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean up s
        # get all alphabets converted to lowercase
        s = "".join([c.lower() for c in list(s) if c.isalnum()])
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True



























        # s = ''.join([c.lower() for c in s if c.isalnum()])
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True
        