class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        # first k
        window = {}
        for i in range(k):
            n = nums[i]
            if n not in window: window[n] = 0
            window[n] += 1

        res = [len(window)]

        # remaining
        for i in range(k, len(nums)):
            left = nums[i - k]
            curr = nums[i]
            if left in window and window[left] == 1:
                del window[left]
            else:
                window[left] -= 1
            if curr not in window: window[curr] = 0
            window[curr] += 1
            # print(window)
            res.append(len(window))
        
        return res
