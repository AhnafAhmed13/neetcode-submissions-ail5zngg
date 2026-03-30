class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lvl = 0
        for log in logs:
            if log == "../":
                lvl = max(0, lvl - 1)
            elif log == "./":
                continue
            else:
                lvl += 1
        return lvl