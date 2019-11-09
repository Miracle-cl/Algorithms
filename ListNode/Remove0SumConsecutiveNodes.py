# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        d = {0: dummy}
        sumval = 0
        p = head
        while p:
            sumval += p.val
            d[sumval] = p
            p = p.next
        # print(list(d.keys()))

        p = dummy
        sumval = 0
        while p:
            sumval += p.val
            p.next = d[sumval].next
            p = p.next
        return dummy.next

    def removeZeroSumSublists_array(self, head: ListNode) -> ListNode:
        arr = []
        sums = [0]
        while head:
            arr.append(head.val)
            sums.append(sums[-1]+head.val)
            head = head.next
            
        n = len(arr)
        i = 0
        dummy = ListNode(-1)
        p = dummy
        while i < n:
            j = n
            while i < j:
                if sums[i] == sums[j]:
                    break
                else:
                    j -= 1
            if i == j:
                p.next = ListNode(arr[i])
                p = p.next
                i += 1
            else:
                i = j
        return dummy.next
