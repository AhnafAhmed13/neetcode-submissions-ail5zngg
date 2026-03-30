class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # return [k for k, _ in Counter(nums).most_common()[:k]]

        n = len(nums)

        num_freq = Counter(nums)

        bucket = [None] * (n + 1)

        for num, freq in num_freq.items():
            if not bucket[freq]:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)

        res = []

        i = n
        while k > 0:
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    k -= 1
                    if k == 0:
                        break
            i -= 1
        
        return res




        