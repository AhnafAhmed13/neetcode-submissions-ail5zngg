class Solution:
    def isDecomposable(self, s: str) -> bool:
        two = 0; curr = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                if curr == 2:
                    two += 1
                    if two > 1: return False
                else:
                    if curr != 3: return False
                curr = 1
            else:
                curr += 1
            if curr == 4:
                curr = 1
        
        if curr == 2:
            two += 1
            if two > 1: return False
        else:
            if curr != 3: return False

        return two == 1