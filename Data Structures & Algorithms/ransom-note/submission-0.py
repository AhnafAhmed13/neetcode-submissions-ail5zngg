class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        c = Counter(magazine)
        for ch in ransomNote:
            if ch not in c or c[ch] == 0:
                return False
            c[ch] -= 1
        return True