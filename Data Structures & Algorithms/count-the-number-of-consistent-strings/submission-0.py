class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed_chars = set()
        for ch in allowed:
            allowed_chars.add(ch)
            
        res = 0
        for word in words:
            chars = set(word)
            for ch in chars:
                if ch not in allowed_chars:
                    break
            else:
                res += 1
        
        return res