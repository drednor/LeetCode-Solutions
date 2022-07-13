"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        result = {}
        def dfs(node):
            if node in result:
                return result[node]
            
            new_node = Node(node.val)
            result[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)       
        
        # print("og=",node)
        # edges = []
        # result = {}
        # visited = set()
        # stack = [node]
        # while stack:
        #     cur = stack.pop()
        #     if cur.val not in visited:
        #         visited.add(cur.val)
        #     else:
        #         continue
        #     for edge in cur.neighbors:
        #         stack.append(edge)
        #         if cur.val not in result:
        #             result[cur.val] = []
        #         result[cur.val].append(edge.val)
        #         edges.append((cur.val, edge.val))
                