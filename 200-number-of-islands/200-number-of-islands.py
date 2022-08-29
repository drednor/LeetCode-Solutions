class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        def bfs(r,c):
            if 0<=r<rows and 0<=c<cols and (r,c) not in visited and grid[r][c] == "1":
                visited.add((r,c))
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r,c-1)
            return
                
                
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    count+=1
        return count

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         rows = len(grid)
#         cols = len(grid[0])
#         visited = set()
#         count = 0
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] != "0":
#                     if self.explore(grid, r, c, visited):
#                         count +=1
#         return count
    
#     def explore(self, grid, r, c, visited):
#         if 0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in visited and grid[r][c] != "0":
#             visited.add((r,c))
#             self.explore(grid,r+1,c,visited)
#             self.explore(grid,r,c+1,visited)
#             self.explore(grid,r-1,c,visited)
#             self.explore(grid,r,c-1,visited)
#             return True
#         return False