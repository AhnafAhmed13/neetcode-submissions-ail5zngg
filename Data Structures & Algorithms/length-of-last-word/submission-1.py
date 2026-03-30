class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if end != -1:
                    return (end - i)
            else:
                if end == -1:
                    end = i
        return end + 1