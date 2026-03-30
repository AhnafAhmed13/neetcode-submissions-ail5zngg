class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            changes = 0
            temp = arr[:]
            for i in range(1, len(temp) - 1):
                if temp[i] < arr[i - 1] and temp[i] < arr[i + 1]:
                    temp[i] += 1
                    changes += 1
                if temp[i] > arr[i - 1] and temp[i] > arr[i + 1]:
                    temp[i] -= 1
                    changes += 1
            arr = temp
            if changes == 0:
                return arr
            