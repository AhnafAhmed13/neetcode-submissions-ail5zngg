class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
        for ch in s:
            if ch not in {'a','e','i','o','u'}:
                res.append(ch)
        return ''.join(res)
