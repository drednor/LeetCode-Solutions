class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in stones:
            graph[i].append((i,j))
            graph[~j].append((i,j))
        
        visited = set()
        count = 0
        for i, j in stones:
            if (i,j) not in visited:
                count+=1
                stack = [(i,j)]
                visited.add((i,j))
                
                while stack:
                    r, c = stack.pop()
                    
                    for x, y in graph[r]:
                        if (x,y) not in visited:
                            stack.append((x,y))
                            visited.add((x,y))
                    
                    for x, y in graph[~c]:
                        if (x,y) not in visited:
                            stack.append((x,y))
                            visited.add((x,y))
        return len(stones) - count