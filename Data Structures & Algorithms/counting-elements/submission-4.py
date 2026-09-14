class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = set(arr)
        res = 0
        for i in range(len(arr)):
            if arr[i] + 1 in a:
                res += 1
        return res