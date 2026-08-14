class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] == arr[-1]:
            return arr[0]

        step = (arr[-1] - arr[0]) // len(arr)
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != step:
                return arr[i - 1] + step