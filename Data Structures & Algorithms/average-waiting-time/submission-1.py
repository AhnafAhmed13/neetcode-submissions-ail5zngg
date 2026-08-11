class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #   1 2 3 4 5 6 7 8 9 0
        # 1 . .
        # 2   _ . . . . .
        # 3       _ _ _ _ . . .

        wait = customers[0][1]
        t = customers[0][0] + customers[0][1]
        for arrive, time in customers[1:]:
            curr = time
            if arrive < t: # wait
                curr += (t - arrive)
            wait += curr
            t = arrive + curr
        return wait / len(customers)

