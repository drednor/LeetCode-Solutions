"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        temp = []
        while cur:
            if cur.child:
                if cur.next:
                    temp.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
            if cur.next == None and len(temp) != 0:
                cur.next = temp.pop()
                cur.next.prev = cur
            cur = cur.next
        return head
                    