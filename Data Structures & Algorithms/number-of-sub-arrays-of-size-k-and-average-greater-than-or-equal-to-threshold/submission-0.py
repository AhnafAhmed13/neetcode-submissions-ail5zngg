class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0

        curr_sum = sum(arr[:k])
        if curr_sum / k >= threshold:
            res += 1

        for i in range(k, len(arr)):
            curr_sum = curr_sum - arr[i - k] + arr[i]
            if curr_sum / k >= threshold:
                res += 1

        return res
        