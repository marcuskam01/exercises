class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import heapq
        #build min heap from distance
        #remove top kth based on distance 
        sol = []
        # min_heap = []
        # for pt in points:
        #     #sqrt is mathematically correct but not necessary
        #     #dist = sqrt(pt[0]**2 + pt[1]**2)
        #     dist = pt[0]**2 + pt[1]**2
        #     heapq.heappush(min_heap, (dist, pt[0], pt[1]))

        #alternative: use heapify instead of pushing to min heap
        min_heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(min_heap)

        for i in range(k):
            sol.append(heapq.heappop(min_heap)[1:])

        return sol