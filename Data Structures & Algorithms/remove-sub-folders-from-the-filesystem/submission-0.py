class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = set(folder)
        for path in folder:
            if path in res:
                marks = set([])
                for other in res:
                    if other != path and other.startswith(path) and other[len(path)] == "/":
                        marks.add(other)
                for mark in marks:
                    res.remove(mark)
        return list(res)
