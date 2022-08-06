class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            x, y = point
            temp = (x**2) + (y**2)
            #heapq.heappush(res, (temp, point))
            res.append([temp, x, y])
        heapq.heapify(res)
        result = []
        while k > 0:
            temp, x, y = heapq.heappop(res)
            result.append([x,y])
            k-=1
        return result