class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if not s:
            return len(s)
        
        if not t:
            return 0
        
        ps, pt = 0, 0

        while ps < len(s):
            if s[ps] == t[pt]:
                pt += 1
                if pt == len(t):
                    return 0
            ps += 1
        
        return len(t) - pt