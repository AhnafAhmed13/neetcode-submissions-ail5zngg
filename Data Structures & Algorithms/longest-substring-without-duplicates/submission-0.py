class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        char_map = { s[0]: 0 }
        res = 1

        left = 0

        for right in range(1, len(s)):

            char = s[right]

            if char in char_map:

                idx = char_map[char]

                if idx >= left:

                    left = idx + 1
            
            char_map[char] = right
            
            res = max(res, right - left + 1)

        return res
            
        