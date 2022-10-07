class MyCalendarThree:

    def __init__(self):
        self.check = defaultdict(int)
        
    def book(self, start: int, end: int) -> int:
        self.check[start] += 1
        self.check[end] -= 1
        res = 0
        inter = 0
        for key in sorted(self.check):
            inter += self.check[key]
            res = max(res, inter)
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)