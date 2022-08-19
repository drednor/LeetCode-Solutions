class DetectSquares:

    def __init__(self):
        self.points =[]
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x, y in self.points:
            if (abs(x-x1) != abs(y-y1)) or x == x1 or y == y1:
                continue
            res += self.ptsCount[(x1,y)] * self.ptsCount[(x,y1)]
        return res
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)