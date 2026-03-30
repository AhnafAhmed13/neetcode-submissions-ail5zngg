from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums
        self.counts = Counter(nums)
        self.uniques = []
        for n in nums:
            if self.counts[n] == 1:
                self.uniques.append(n)

    def showFirstUnique(self) -> int:
        return self.uniques[0] if self.uniques else -1

    def add(self, value: int) -> None:
        self.q.append(value)
        if value in self.uniques:
            self.uniques.remove(value)
        else:
            self.uniques.append(value)
        self.counts[value] = 1 + self.counts.get(value, 0)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
