class Solution:
    from collections import defaultdict
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums2)):
            hashmap[nums2[i]].append(i)
        res = []
        for i in range(len(nums1)):
            res.append(hashmap[nums1[i]].pop(0))
        return res