class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        l = 0; res = 0; curr = {}
        for r in range(len(s)):
            ch = s[r]; curr[ch] = 1 + curr.get(ch, 0)
            if len(curr) > k:
                while l < r:
                    left = s[l]; l += 1; curr[left] -= 1
                    if curr[left] == 0:
                        del curr[left]; break
            res = max(res, r - l + 1)
        return res