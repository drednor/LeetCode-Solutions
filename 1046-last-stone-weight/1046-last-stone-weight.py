class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            temp = abs(x) - abs(y)
            if temp != 0:
                temp *= -1
                heapq.heappush(stones,temp)
        if len(stones) < 1:
            return 0
        return -1*stones[0]
        