class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position,speed)]
        stack =[]
        for p,s in sorted(pair, reverse=True):
            temp = (target - p)/s
            if stack and stack[-1] >= temp:
                continue
            stack.append(temp)
        return len(stack)