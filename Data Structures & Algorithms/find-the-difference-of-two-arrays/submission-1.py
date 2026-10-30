class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = list(set(nums1).difference(set(nums2)))
        res2 = list(set(nums2).difference(set(nums1)))
        return [res1, res2]