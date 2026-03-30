class Solution:

    def merge(self, nums1, nums2):
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged.extend(nums1[i:])
        if j < len(nums2):
            merged.extend(nums2[j:])
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        

        # Merge sort
        def merge_sort(left, right):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2
            return self.merge(merge_sort(left, mid), merge_sort(mid + 1, right))

        return merge_sort(0, len(nums) - 1)


        # Bubble sort
        # for i in range(len(nums) - 1):
        #     swaps = 0
        #     for j in range(len(nums) - 1 - i):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swaps += 1
        #     if swaps == 0:
        #         break
        # return nums


        # Insertion sort
        # for i in range(len(nums)):
        #     for j in range(i, 0, -1):
        #         if nums[j - 1] > nums[j]:
        #             nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #         else:
        #             break
        # return nums


        # Selection sort
        # for i in range(len(nums)):
        #     curr_min = i
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[curr_min]:
        #             curr_min = j
        #     nums[i], nums[curr_min] = nums[curr_min], nums[i]
        # return nums