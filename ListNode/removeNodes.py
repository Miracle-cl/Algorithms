class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class S:
    def create_list(self, arr):
        # arr : list
        dummy = ListNode(-1)
        p = dummy
        for x in arr:
            p.next = ListNode(x)
            p = p.next
        return dummy.next

    def remove_nodes(self, head, k):
        prev = head
        cur = head
        i = 0
        while cur:
            cur = cur.next
            i += 1
            if i >= k:
                break
        if not cur:
            return prev.next
        while cur.next:
            prev = prev.next
            cur = cur.next
        prev.next = prev.next.next
        return head

    def print_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

ss = S()
p = ss.create_list([1,2,3,4,5])
q = ss.remove_nodes(p, 2)
ss.print_list(q)
