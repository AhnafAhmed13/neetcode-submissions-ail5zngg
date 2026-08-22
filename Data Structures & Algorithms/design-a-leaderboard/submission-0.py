class Leaderboard:

    from collections import defaultdict, heapq

    def __init__(self):
        self.score = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.score[playerId] += score

    def top(self, K: int) -> int:
        vals = list(self.score.values())
        if K == 1: return max(vals)
        if K >= len(self.score): return sum(vals)
        heap = vals[:K]
        heapq.heapify(heap)
        for i in range(K, len(vals)):
            heapq.heappush(heap, vals[i])
            heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
