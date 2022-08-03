class MyCalendar:

    def __init__(self):
        # self.res = set()
        self.res = []
        
    def book(self, start: int, end: int) -> bool:
        if len(self.res) == 0:
            self.res.append((start,end))
            return True
        for i in range(len(self.res)):
            if self.res[i][0] <= start < end <= self.res[i][1]:
                return False
            if start <= self.res[i][0] < end <= self.res[i][1]:
                return False
            if self.res[i][0] <= start < self.res[i][1] < end:
                return False
            if start <= self.res[i][0] < self.res[i][1] < end:
                return False
        self.res.append((start,end))
        return True
        
        
        
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