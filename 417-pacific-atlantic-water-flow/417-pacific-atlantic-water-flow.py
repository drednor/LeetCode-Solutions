class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []
        atl, pac = set(), set()
        
        def dfs(r, c, visited, prevheight):
            if 0<=r<rows and 0<=c<cols and (r,c) not in visited and heights[r][c]>=prevheight:
                visited.add((r,c))
                dfs(r+1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    result.append([r,c])
        return result
    
    
    