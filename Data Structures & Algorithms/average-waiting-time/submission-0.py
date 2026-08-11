class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #   1 2 3 4 5 6 7 8 9 0
        # 1 . .
        # 2   _ . . . . .
        # 3       _ _ _ _ . . .

        wait = customers[0][1]
        end = [customers[0][0] + customers[0][1]]
        for i in range(1, len(customers)):
            arrive, time = customers[i]
            curr = time
            if arrive < end[-1]: # wait
                curr += (end[-1] - arrive)
            wait += curr
            end.append(arrive + curr)
        return wait / len(customers)

