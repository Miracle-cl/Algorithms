class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeSortList(self, head):
        if (not head or not head.next):
            return head
        slow = head
        fast = head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return self.Merge(self.mergeSortList(head), self.mergeSortList(head2))

    def Merge(self, p1, p2):
        dummy = ListNode(-1)
        cur = dummy
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return dummy.next

    # insertion sort
    def insertionSortList(self, head):
        sorted_list = ListNode(-1)
        while head:
            cur = sorted_list
            while (cur.next and cur.next.val < head.val):
                cur = cur.next
            nxt = cur.next
            cur.next = head
            head = head.next
            cur.next.next = nxt
        return sorted_list.next

    def create_list(self, array):
        dummy = ListNode(-1)
        p = dummy
        for n in array:
            p.next = ListNode(n)
            p = p.next
        return dummy.next


if __name__ == "__main__":
    arr = [4,2,1,3,3]
    s = Solution()
    head = s.create_list(arr)
    # head2 = s.insertionSortList(head)
    head2 = s.mergeSortList(head)
    while head2:
        print(head2.val)
        head2 = head2.next
