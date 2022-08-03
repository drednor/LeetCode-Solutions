class MyCalendar:

    def __init__(self):
        # self.res = set()
        self.res = [(0,0),(10**9,10**9)]
        
    def book(self, start: int, end: int) -> bool:
        l , r = 0, len(self.res)
        while l < r:
            mid = (l+r)//2
            if self.res[mid][0] == end:
                l = mid
                break
            elif self.res[mid][0] < end:
                l = mid + 1
            else:
                r = mid
        if start<self.res[l-1][1]: return False
        self.res.insert(l,(start,end))
        return True
        
        
        # if len(self.res) == 0:
        #     self.res.append((start,end))
        #     return True
        # for i in range(len(self.res)):
        #     if self.res[i][0] <= start < end <= self.res[i][1]:
        #         return False
        #     if start <= self.res[i][0] < end <= self.res[i][1]:
        #         return False
        #     if self.res[i][0] <= start < self.res[i][1] < end:
        #         return False
        #     if start <= self.res[i][0] < self.res[i][1] < end:
        #         return False
        # self.res.append((start,end))
        # return True
        
        
        
        # if start in self.res:
        #     return False
        # temp = set()
        # for i in range(start, end):
        #     if i in self.res:
        #         return False
        #     temp.add(i)
        # self.res.update(temp)
        # return True
    


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)