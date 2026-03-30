class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        counts = Counter(s)
        freqs = Counter(list(counts.values()))
        odd = False
        for freq in freqs:
            if freq % 2 == 1:
                if odd or freqs[freq] > 1:
                    return False
                odd = True
        return True