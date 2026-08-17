class Solution:
    def countLetters(self, s: str) -> int:

        groups = {}
        curr = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr += 1
            else:
                groups[curr] = groups.get(curr, 0) + 1
                curr = 1
        groups[curr] = groups.get(curr, 0) + 1

        res = 0
        dp = {}
        for i, n in groups.items():
            if i not in dp:
                dp[i] = (i * (i + 1)) // 2
            res += dp[i] * n

        return res