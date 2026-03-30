from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums
        self.u = nums[:]
        self.counts = Counter(nums)

    def showFirstUnique(self) -> int:
        for i, n in enumerate(self.u):
            if self.counts[n] == 1:
                self.u = self.u[i:]
                return n
        return -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.u.append(value)
        self.counts[value] = 1 + self.counts.get(value, 0)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
