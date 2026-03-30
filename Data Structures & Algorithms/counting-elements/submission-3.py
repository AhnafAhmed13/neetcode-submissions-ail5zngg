class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter
        res = 0
        s_arr = set(arr)
        for n in arr:
            if n + 1 in s_arr:
                res += 1
        return res