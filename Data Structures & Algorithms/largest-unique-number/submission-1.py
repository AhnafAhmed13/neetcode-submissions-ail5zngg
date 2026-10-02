class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set(); dups = set()
        for n in nums:
            if n in seen: dups.add(n)
            seen.add(n)
        res = None
        for n in nums:
            if n not in dups:
                if not res: res = n
                res = max(res, n)
        return res if res else -1