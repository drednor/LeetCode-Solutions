class MyCalendarThree:

    def __init__(self):
        self.bookings = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.bookings[start] += 1
        self.bookings[end] -= 1
        
        res = 0
        inter = 0
        for key in sorted(self.bookings):
            inter += self.bookings[key]
            res = max(res, inter)
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)