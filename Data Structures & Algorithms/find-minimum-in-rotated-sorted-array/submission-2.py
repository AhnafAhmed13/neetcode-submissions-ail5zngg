class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        input - nums: list -> rotated sorted array
        output - int -> minimum
        constraint - O(log n)
        edge case - already sorted -> first < last
                    return first
                    
                    if only 1 elt -> return elt

        plan - [...last < first...]
                left < mid < right
                [3,4,5,6,1,2]
                     m
                mid > right? -> right half
                mid < left? -> left half


        while l < r
            m = (l + r) // 2
            m - 1 > m:
                return m
            if m > r:
                l = m + 1
            elif m < l:
                r = m
        '''

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1