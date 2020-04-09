class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create_ln(self, arr):
        dummy = ListNode(-1)
        p = dummy
        for x in arr:
            p.next = ListNode(x)
            p = p.next
        return dummy.next

    def reverseKGroup(self, head, k):
        # head : ListNode 1 2 3 4 5
        # k : K group 2
        # output => 2 1 4 3 5
        if (not head) or (not head.next) or (k < 2) :
            return head
        size = 0
        p = head
        while (p):
            p = p.next
            size += 1

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(size // k):
            cur = prev.next
            nxt = cur.next
            for _ in range(k-1):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next
            prev = cur
        return dummy.next

arr = [1, 2, 3, 4, 5, 6, 7]
ss = Solution()
p = ss.create_ln(arr)
p = ss.reverseKGroup(p, 3)
while p:
    print(p.val)
    p = p.next
