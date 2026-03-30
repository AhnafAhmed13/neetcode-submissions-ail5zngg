class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {
                    "0": "0",
                    "1": "1",
                    "6": "9",
                    "8": "8",
                    "9": "6"
                }

        res = []
        for i in str(n):
            if i not in rotate:
                return False
            res.append(rotate[i])
        
        return str(n) != ''.join(res[::-1])