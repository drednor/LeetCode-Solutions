class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations += [[target, 0]]
        heap = []
        res = 0
        prev = 0
        fuel = startFuel
        for pos, gas in stations:
            fuel -= (pos - prev)
            while heap and fuel< 0:
                x = heappop(heap)
                fuel += (-1*x)
                res += 1
            if fuel < 0:
                return -1
            heappush(heap, -gas)
            prev = pos
        return res