class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        plus = 0 
        g = deque(str(n))
        for i in g:
            prod *= int(i)
            plus += int(i)
        return prod-plus
        