class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = set()
        inv_rows = set()
        cols = set()
        inv_cols = set()
        blacks = []
        for r in range(len(picture)):
            for c in range(len(picture[r])):
                curr = picture[r][c]
                if curr == "B":
                    if r in rows:
                        inv_rows.add(r)
                    if c in cols:
                        inv_cols.add(c)
                    rows.add(r)
                    cols.add(c)
                    blacks.append((r, c))
        res = 0
        for r, c in blacks:
            if r not in inv_rows and c not in inv_cols:
                res += 1

        return res