# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if cur.child:
                nxt = cur.next
                chd = cur.child
                while chd.next:
                    chd = chd.next
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                chd.next = nxt
                if nxt:
                    nxt.prev = chd
            cur = cur.next
        return head
