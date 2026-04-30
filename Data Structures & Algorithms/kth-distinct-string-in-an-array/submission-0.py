class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = set()
        dist = set()
        for s in arr:
            if s in seen:
                if s in dist:
                    dist.remove(s)
            else:
                dist.add(s)
            seen.add(s)
        count = 0
        for s in arr:
            if s in dist:
                count += 1
                if count == k:
                    return s
        
        return ""