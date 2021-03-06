class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.array = nums
        heapq.heapify(self.array)
        while len(self.array) > k:
            heapq.heappop(self.array)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.array,val)
        if len(self.array) > self.k:
            heapq.heappop(self.array)
        return self.array[0]
                
        
        
        # l, r  = 0 , len(self.array)-1
        # while l <= r:
        #     mid = (l+r)//2
        #     if val == self.array[mid]:
        #         l = mid
        #         break
        #     elif val > self.array[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # self.array.insert(l, val)
        # # print(self.array)
        # return self.array[len(self.array) - (self.k)]
        # self.array.append(val)
        # self.array.sort(reverse=True)
        # return self.array[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)