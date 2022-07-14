class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        visited = set()
        cycle = set()
        result = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            if crs not in result:
                result.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result