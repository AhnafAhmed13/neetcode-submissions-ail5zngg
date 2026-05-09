class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        def dfs(r, c):
            nonlocal seen
            
            if (r, c) in seen or not 0 <= r < m or not 0 <= c < n:
                return

            seen.add((r, c))

            if image[r][c] != original:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
            
