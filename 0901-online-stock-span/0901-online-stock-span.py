class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            span += self.prices[-1][1]
            self.prices.pop()
        self.prices.append((price, span))
        return span

        # if self.prices and price >= self.prices[-1]:
        #     n = len(self.prices)
        #     i = n-1
        #     ans = 1
        #     while i >= 0:
        #         temp = self.prices[i]
        #         if price >= temp:
        #             ans+=1
        #             i-=1
        #         else:
        #             break
        #     self.prices.append(price)
        #     return ans
        # else:
        #     self.prices.append(price)
        #     return 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)