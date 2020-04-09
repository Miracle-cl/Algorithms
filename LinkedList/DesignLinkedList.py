class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        node = ListNode(val)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            cur.next = cur.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
print('param_1: ', param_1)
obj.addAtHead(1)
obj.addAtTail(5)
obj.addAtIndex(1, 3)
# obj.deleteAtIndex(index)
for i in range(4):
    print(obj.get(i))
