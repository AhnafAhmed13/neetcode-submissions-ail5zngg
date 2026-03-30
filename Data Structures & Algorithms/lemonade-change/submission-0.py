class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0, 0] # 5, 10
        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if changes[0] == 0:
                    return False
                changes[0] -= 1
                changes[1] += 1
            else: # 20
                if changes[1] == 0: # 3 5s
                    if changes[0] < 3:
                        return False
                    changes[0] -= 3
                else: # 1 5s + 1 10s
                    if changes[0] == 0:
                        return False
                    changes[0] -= 1
                    changes[1] -= 1
        return True
                
