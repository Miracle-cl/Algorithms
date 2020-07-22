from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
            
        def merge2list(l1, l2):
            dummy = ListNode(-1)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            if l1:
                cur.next = l1
                
            if l2:
                cur.next = l2
            return dummy.next
        
        def mergelists(left, right):
            if left >= right:
                return lists[left]
            mid = (left + right) // 2
            return merge2list(mergelists(left, mid), mergelists(mid+1, right))
            
        merged = mergelists(0, len(lists)-1)
        return merged

    def mergeKLists_heap(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        q = []
        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(q, (node.val, i))

        dummy = ListNode(-1)
        cur = dummy
        while q:
            _, i = heapq.heappop(q)
            if lists[i].next:
                heapq.heappush(q, (lists[i].next.val, i))
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
        return dummy.next