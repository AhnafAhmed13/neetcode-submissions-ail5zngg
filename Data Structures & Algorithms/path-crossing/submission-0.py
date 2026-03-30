class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        visited.add((0, 0))
        for p in path:
            if p == "N":
                x -= 1
            elif p == "S":
                x += 1
            elif p == "E":
                y += 1
            else:
                y -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False