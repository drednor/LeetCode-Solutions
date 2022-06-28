class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        for i , n in enumerate(heights):
            start = i
            while stack and n < stack[-1][1]:
                idx, tops = stack.pop()
                ans = (i - idx)*tops
                result = max(ans, result)
                start = idx
            stack.append([start, n])
            
        while stack:
            idx, tops = stack.pop()
            ans = (len(heights) - idx)*tops
            result = max(ans, result)
        return result