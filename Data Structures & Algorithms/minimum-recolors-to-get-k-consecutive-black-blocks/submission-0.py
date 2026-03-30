class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        blacks = 0
        for block in blocks[:k]:
            if block == "W":
                whites += 1
            else:
                blacks += 1
        
        res = whites
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == "W":
                whites -= 1
            else:
                blacks -= 1

            if blocks[i + k - 1] == "W":
                whites += 1
            else:
                blacks += 1
                
            res = min(res, whites)

        return res