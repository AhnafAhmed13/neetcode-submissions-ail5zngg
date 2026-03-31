class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied = sum([customers[i] for i in range(minutes) if grumpy[i] == 1])
        max_unsatisfied = unsatisfied
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                unsatisfied -= customers[i - minutes]
            if grumpy[i] == 1:
                unsatisfied += customers[i]
            if unsatisfied > max_unsatisfied:
                max_unsatisfied = unsatisfied
        res = max_unsatisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
        return res
