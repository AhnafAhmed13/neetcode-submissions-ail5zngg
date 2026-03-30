class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # base case
        if k == 0:
            return False

        # for the first k
        s = set()
        for n in nums[:k+1]:
            if n in s:
                return True
            s.add(n)
        
        # rest
        l = 0
        r = k + 1
        while r < len(nums):
            left = nums[l]
            s.remove(left)

            right = nums[r]
            if right in s:
                return True
            s.add(right)
            l += 1
            r += 1

        return False
