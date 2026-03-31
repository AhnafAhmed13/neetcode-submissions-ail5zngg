class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Pre-compute first 'minutes' customers
        satisfied, unsatisfied = 0, 0
        for i in range(minutes):
            if grumpy[i]:
                unsatisfied += customers[i]
            else:
                satisfied += customers[i]
        # Sliding window
        max_unsatisfied = unsatisfied
        for i in range(minutes, len(customers)):
            # Remove from window
            if grumpy[i - minutes]:
                unsatisfied -= customers[i - minutes]
            # Add to window
            if grumpy[i]:
                unsatisfied += customers[i]
            else:
                satisfied += customers[i]
            # Update max window
            max_unsatisfied = max(max_unsatisfied, unsatisfied)
        return satisfied + max_unsatisfied
