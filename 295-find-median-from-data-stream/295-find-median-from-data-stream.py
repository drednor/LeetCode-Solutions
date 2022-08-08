class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num)
        
        if self.small and self.large and (-1* self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        
        # def binarysearch(num):
        #     l , r = 0 , len(self.arr)-1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if self.arr[mid] > num:
        #             r = mid -1
        #         elif self.arr[mid] < num:
        #             l = mid + 1 
        #         else:
        #             return mid
        #     return l
        # pos = binarysearch(num)
        # self.arr.insert(pos, num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1*self.small[0] + self.large[0])/2
        # x = len(self.arr)
        # if x % 2:
        #     return self.arr[x//2]
        # else:
        #     i = x//2
        #     temp = self.arr[i]
        #     if i-1 >= 0:
        #         temp += self.arr[i-1]
        #     return temp/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()