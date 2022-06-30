"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtocopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            new = oldtocopy[cur]
            new.next = oldtocopy[cur.next]
            new.random = oldtocopy[cur.random]
            cur = cur.next
        return oldtocopy[head]
         ###interweave
#         dummy = Node(-1)
#         dummy.next = head
#         cur = head
#         while cur:
#             temp = Node(cur.val)
#             temp.next = cur.next
#             cur.next = temp
#             cur = temp.next
        
#         cur = head
#         while cur:
#             if cur.random:
#                 cur.next.random = cur.random.next
#             cur = cur.next.next
        
#         cur = dummy
#         old = head
        
#         while old:
#             cur.next = old.next
#             cur = old
#             old = cur.next
#         return dummy.next
        
         
        ### USING A HASH MAP
#         oldtocopy ={None:None}
#         cur = head
#         while cur:
#             copy = Node(cur.val)
#             oldtocopy[cur] = copy
#             cur = cur.next
            
    
#         cur = head
#         while cur:
#             copy = oldtocopy[cur]
#             copy.next = oldtocopy[cur.next]
#             copy.random = oldtocopy[cur.random]
#             cur = cur.next
#         return oldtocopy[head]
        
        