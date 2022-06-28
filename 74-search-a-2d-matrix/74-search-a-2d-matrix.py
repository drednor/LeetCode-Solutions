class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        
        top = 0 
        bot = rows -1
        
        while top <= bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else: break
        
        if not (top<= bot):
            return False
        row = (top+bot)//2
        l = 0 
        r = len(matrix[row]) - 1
        while l<=r:
            mid = l+((r-l)//2)
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid +1
        return False
        