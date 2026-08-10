class Solution:
    from collections import Counter
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        res = sum(counts.values())
        odds = 0
        for freq in counts.values():
            if freq % 2 != 0:
                odds += 1
        if odds > 1:
            res -= (odds - 1)
        return res
