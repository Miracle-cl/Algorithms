class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create_list(self, array):
        dummy = ListNode(-1)
        p = dummy
        for n in array:
            p.next = ListNode(n)
            p = p.next
        return dummy.next

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        idx = 1
        p = head
        first = ListNode(-1)
        second = ListNode(-1)
        odd = first
        even = second
        while p:
            if idx % 2 == 1:
                odd.next = p
                odd = odd.next
            else:
                even.next = p
                even = even.next
            p = p.next
            idx += 1
        odd.next = second.next
        even.next = None
        return first.next

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,7]
    head = s.create_list(arr)
    res = s.oddEvenList(head)
    while (res):
        print(res.val)
        res = res.next
        # break
