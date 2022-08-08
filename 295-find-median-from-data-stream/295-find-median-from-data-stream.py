class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        pos = bisect_left(self.arr, num)
        self.arr.insert(pos, num)

    def findMedian(self) -> float:
        x = len(self.arr)
        if x % 2:
            return self.arr[x//2]
        else:
            i = x//2
            temp = self.arr[i]
            if i-1 >= 0:
                temp += self.arr[i-1]
            return temp/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()