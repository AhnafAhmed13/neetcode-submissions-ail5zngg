class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        from collections import deque
        q = deque(s)
        for d, a in shift:
            if d == 0:
                for _ in range(a):
                    q.append(q.popleft())
            else:
                for _ in range(a):
                    q.appendleft(q.pop())

        return ''.join(q)