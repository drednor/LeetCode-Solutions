class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        check = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if check[i] != heights[i]:
                result+=1
        return result
                