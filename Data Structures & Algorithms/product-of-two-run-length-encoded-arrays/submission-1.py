class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        nums1 = []
        for val, freq in encoded1:
            nums1.extend([val] * freq)
        nums2 = []
        for val, freq in encoded2:
            nums2.extend([val] * freq)
        prod = []
        for i in range(len(nums1)):
            prod.append(nums1[i] * nums2[i])
        # print(prod)
        res = []; curr_freq = 1
        for i in range(1, len(prod)):
            if prod[i - 1] == prod[i]:
                curr_freq += 1
            else:
                res.append([prod[i-1], curr_freq])
                curr_freq = 1
        res.append([prod[-1], curr_freq])
        return res
        
