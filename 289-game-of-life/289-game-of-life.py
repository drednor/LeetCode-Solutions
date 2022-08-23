class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row , col = len(board), len(board[0])
        dead = set()
        live = set()
        def bfs(r,c):
            count = 0
            if 0<=r<row and 0<=c<col and board[r][c] == 1:
                count+=1
            return count 
        
        for i in range(row):
            for j in range(col):
                temp = 0
                temp += bfs(i+1, j)
                temp += bfs(i, j+1)
                temp += bfs(i-1, j)
                temp += bfs(i, j-1)
                temp += bfs(i+1, j+1)
                temp += bfs(i+1, j-1)
                temp += bfs(i-1, j+1)
                temp += bfs(i-1, j-1)
                if board[i][j] == 0 and temp == 3:
                    live.add((i,j))
                elif board[i][j] == 1:
                    if temp < 2:
                        dead.add((i,j))
                    elif temp == 2 or temp == 3:
                        live.add((i,j))
                    elif temp > 3:
                        dead.add((i,j))
        for i in range(row):
            for j in range(col):
                key = (i,j)
                if key in live:
                    board[i][j] = 1
                elif key in dead:
                    board[i][j] = 0
        return None
                
