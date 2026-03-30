class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def update(start, size, val):
            for i in range(start, start + size):
                nums[i] = val
        
        count = Counter(nums)

        offset = 0
        if 0 in count:
            update(start=offset, size=count[0], val=0)
            offset += count[0]

        if 1 in count:
            update(start=offset, size=count[1], val=1)
            offset += count[1]

        if 2 in count:
            update(start=offset, size=count[2], val=2)