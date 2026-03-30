class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq, math

        # heapify whole list
        # return first k elts
        # for i in range(len(points)):
        #     x, y = points[i]
        #     distance = math.sqrt(x**2 + y**2)
        #     points[i] = (distance, [x, y])
        # heapq.heapify(points)
        # res = []
        # for _ in range(k):
        #     _, pts = (heapq.heappop(points))
        #     res.append(pts)
        # return res

        # create max heap with first k elts
        # if new elt is bigger than top, skip
        # else, pop top, push new, heapify
        res = []
        for i in range(k):
            x, y = points[i]
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush_max(res, (distance, [x, y]))
        for x, y in points[k:]:
            distance = math.sqrt(x**2 + y**2)
            if distance < res[0][0]:
                heapq.heappop_max(res)
                heapq.heappush_max(res, (distance, [x, y]))
        return [pts for _, pts in res]

