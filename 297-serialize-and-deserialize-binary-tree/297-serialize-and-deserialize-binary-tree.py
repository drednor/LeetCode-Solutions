# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        # if root is None:
        #     return []
        # stack = [root]
        # result = []
        # while stack:
        #     cur = stack.pop()
        #     result.append(str(cur.val))
        #     if cur.right:
        #         stack.append(cur.right)
        #     else:
        #         result.append("N")
        #     if cur.left:
        #         stack.append(cur.left)
        #     else:
        #         result.append("N")
        # return ",".join(result) 
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
  

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))