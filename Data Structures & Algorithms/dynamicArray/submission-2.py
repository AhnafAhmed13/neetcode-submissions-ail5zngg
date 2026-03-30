class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dynamic_array = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.dynamic_array[i]

    def set(self, i: int, n: int) -> None:
        if not self.dynamic_array[i]:
            self.length += 1
        self.dynamic_array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.dynamic_array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        value = self.dynamic_array[self.length - 1]
        self.dynamic_array[self.length - 1] = None
        self.length -= 1
        return value

    def resize(self) -> None:
        self.dynamic_array.extend([None] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
