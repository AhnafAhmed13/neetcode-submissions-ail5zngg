class Solution:
    def removeVowels(self, s: str) -> str:
        return s.translate(str.maketrans('','','aeiou'))
