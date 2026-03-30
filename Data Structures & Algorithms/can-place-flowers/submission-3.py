class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        counts = []
        curr = 0
        for bed in flowerbed:
            if bed == 0:
                curr += 1
            else:
                counts.append(curr)
                curr = 0
        counts.append(curr)

        if len(counts) == 1:
            return n == (counts[0] + 1) // 2

        if counts[0] > 1:
            n -= counts[0] // 2
            counts = counts[1:]

        if counts[-1] > 1:
            n -= counts[-1] // 2
            counts = counts[:len(counts) - 1]

        for c in counts:
            if c > 2:
                n -= (c - 1) // 2
            
        return n <= 0

        # 001
        # 1
        # 0001
        # 1
        # 00001
        # 1 1

        # 1000001
        #   1 1
        # 10000001
        #   1 1