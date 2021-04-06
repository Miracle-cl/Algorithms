
# Definition for a Node.

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        map = {}

        current = head
        while current:
            map[current] = Node(current.val, None, None)
            current = current.next

        current = head
        while current:
            if current.next:
                map[current].next = map[current.next]
            else:
                map[current].next = None

            if current.random:
                map[current].random = map[current.random]
            else:
                map[current].random = None

            current = current.next

        return map[head]


# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         import copy
#         return copy.deepcopy(head)
