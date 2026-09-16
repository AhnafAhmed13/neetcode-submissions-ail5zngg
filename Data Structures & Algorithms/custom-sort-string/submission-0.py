class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = { c : i for i, c in enumerate(order) }
        res = list(s)
        res.sort(key=lambda x: (order.get(x, len(order)), x))
        return "".join(res)