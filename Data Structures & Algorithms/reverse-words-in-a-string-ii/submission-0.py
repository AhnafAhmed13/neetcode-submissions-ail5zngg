class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # reverse whole string

        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        # reverse each string

        l = 0
        for i in range(len(s)):
            if s[i] == " " or i == len(s) - 1:
                r = i - 1
                if i == len(s) - 1:
                    r = i
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i + 1
        
