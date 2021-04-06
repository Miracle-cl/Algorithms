from heapq import heappush, heappop

class MinHeap:
    """Implement heap by list"""
    def __init__(self):
        self.h = []
        self.size = 0

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def extract_min(self):
        if self.size <= 0:
            return None
        if self.size == 1:
            self.size -= 1
            return self.h.pop()
        root = self.h[0]
        self.size -= 1
        self.h[0] = self.h.pop() # [-1]
        self.min_heapify(0)
        return root

    def decrease_val(self, i, val):
        # val < h[i], change h[i] to val
        self.h[i] = val
        while (i != 0 and self.h[self.parent(i)] > self.h[i]):
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)

    def get_min(self):
        return self.h[0] if self.size else None

    def delete_key(self, i):
        self.decrease_val(i, float('-inf'))
        self.extract_min()

    def push(self, val):
        i = self.size

        self.size += 1
        self.h.append(val)

        while (i != 0 and self.h[self.parent(i)] > self.h[i]):
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)

    def min_heapify(self, i):
        ll = self.left(i)
        rr = self.right(i)
        small = i

        if ll < self.size and self.h[ll] < self.h[small]:
            small = ll

        if rr < self.size and self.h[rr] < self.h[small]:
            small = rr

        if small != i:
            self.h[i], self.h[small] = self.h[small], self.h[i]
            self.min_heapify(small)


class MinHeapq:
    """Implement heap by heapq"""
    def __init__(self):
        self.h = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def push(self, val):
        heappush(self.h, val)

    def get_min(self):
        return self.h[0] if self.h else None

    def extract_min(self):
        if self.h:
            return heappop(self.h)
        else:
            return None

    def decrease_val(self, i, val):
        # val < h[i], change h[i] to val
        self.h[i] = val
        while (i != 0 and self.h[self.parent(i)] > self.h[i]):
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)

    def delete_key(self, i):
        self.decrease_val(i, float('-inf'))
        self.extract_min()


if __name__ == '__main__':
    mh = MinHeap() # Implement heap by list
    # mh = MinHeapq() # Implement heap by heapq
    mh.push(3)
    mh.push(2)
    mh.delete_key(1)
    print(mh.h)

    mh.push(15)
    mh.push(5)
    mh.push(4)
    mh.push(45)
    print(mh.h)
    print(mh.extract_min())
    print(mh.h)
    print(mh.get_min())

    mh.decrease_val(2, 1)
    print(mh.h)
    print(mh.get_min())
