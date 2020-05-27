class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        node = ListNode(key, value)
        self._add(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            h = self.head.next
            self._remove(h)
            del self.d[h.key]
        
    def _remove(self, node: ListNode):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def _add(self, node: ListNode):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache1:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True) # move to right
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) # FIFO