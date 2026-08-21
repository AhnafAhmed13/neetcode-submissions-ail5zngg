class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = 0
        self.v = []
        for i in range(min(len(v1), len(v2))):
            self.v.append(v1[i])
            self.v.append(v2[i])
        l = len(self.v) // 2
        if l < len(v1): self.v.extend(v1[l:])
        else: self.v.extend(v2[l:])

    def next(self) -> int:
        if self.hasNext():
            val = self.v[self.i]
            self.i += 1
            return val

    def hasNext(self) -> bool:
        return self.i < len(self.v)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
