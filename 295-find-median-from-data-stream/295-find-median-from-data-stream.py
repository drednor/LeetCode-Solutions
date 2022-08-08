class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        def binarysearch(num):
            l , r = 0 , len(self.arr)-1
            while l <= r:
                mid = (l+r)//2
                if self.arr[mid] > num:
                    r = mid -1
                elif self.arr[mid] < num:
                    l = mid + 1 
                else:
                    return mid
            return l
        pos = binarysearch(num)
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