class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num) - 2):
            curr = num[i:i+3]
            if curr[0] == curr[1] == curr[2]:
                if res == "" or int(curr[0]) > int(res[0]):
                    res = curr
        return res