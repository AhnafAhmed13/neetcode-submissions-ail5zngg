class Solution:
    from collections import Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for char, freq in rc.items():
            if char not in mc:
                return False
            if mc[char] < freq:
                return False
        return True