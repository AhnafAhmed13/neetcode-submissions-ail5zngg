class Solution:
    def isPalindrome(self, s: str) -> bool:

        # stack
        s = ''.join([c.lower() for c in s if c.isalnum()])
        if not s: return True
        stack = []
        for i in range(len(s) // 2 + 1):
            stack.append(s[i])
        
        for i in range(len(s) - 1, len(s) // 2 - 1, -1):
            p = stack.pop(0)
            if s[i] != p:
                return False

        return True

        # 2 pointers
        # s = ''.join([c.lower() for c in s if c.isalnum()])
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True
        