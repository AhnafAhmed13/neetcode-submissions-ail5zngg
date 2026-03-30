class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        for char in t:
            if char not in counter_s:
                return False
            else:
                if counter_s[char] == 1:
                    del counter_s[char]
                else:
                    counter_s[char] -= 1
                    
        if len(counter_s) > 0: return False

        return True
        