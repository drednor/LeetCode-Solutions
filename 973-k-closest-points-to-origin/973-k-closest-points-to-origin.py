class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            x, y = point
            temp = (x**2) + (y**2)
            heapq.heappush(res, (temp, point))
        result = []
        while k > 0:
            temp, point = heapq.heappop(res)
            result.append(point)
            k-=1
        return result