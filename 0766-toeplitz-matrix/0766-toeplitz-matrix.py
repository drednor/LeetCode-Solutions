class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                temp = matrix[i][j]
                if i+1 < n and j+1 < m:
                    if temp != matrix[i+1][j+1]:
                        return False
        return True
                    
                    
                
                