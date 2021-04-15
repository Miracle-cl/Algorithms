class MaxHeap:
    def __init__(self, max_items):
        self.idx_ = [-1] * max_items
        self.vals_ = [None] * max_items
        self.size_ = 0
        
    def add(self, key: int, i: int):
        self.idx_[i] = self.size_
        self.vals_[self.size_] = (key, i)
        self.size_ += 1
        self._heapify_up(i)

    def remove(self, i: int):
        evict_id = self.idx_[i]
        self._swap_node(evict_id, self.size_ - 1)
        self.size_ -= 1
        self._heapify_down(evict_id)
    
    def empty(self):
        return self.size_ == 0

    def get_max(self):
        return 0 if self.empty() else self.vals_[0][0]
    
    def _heapify_up(self, i):
        while i > 0:
            p = (i - 1) // 2 # parent
            if self.vals_[p][0] >= self.vals_[i][0]:
                return
            self._swap_node(p, i)
            i = p

    def _heapify_down(self, i):
        # left & right children
        c1 = 2 * i + 1
        c2 = 2 * i + 2
        if c1 >= self.size_:
            return

        # get id of the max child
        c = c2 if c2 < self.size_ and self.vals_[c2][0] > self.vals_[c1][0] else c1
        if self.vals_[c][0] <= self.vals_[i][0]:
            return
        self._swap_node(c, i)
        self._heapify_down(c)

    def _swap_node(self, i, j):
        self.idx_[self.vals_[i][1]], self.idx_[self.vals_[j][1]] = \
            self.idx_[self.vals_[j][1]], self.idx_[self.vals_[i][1]]
        self.vals_[i], self.vals_[j] = self.vals_[j], self.vals_[i]
        
    def __repr__(self):
        return f"ids: {self.idx_}\nvals: {self.vals_}"


if __name__ == '__main__':
    xx = [(5,0),(7,1),(3,2),(1,3),(9,4),]

    mh = MaxHeap(5)
    for k, i in xx:
        mh.add(k, i)
        print(mh)

    mh.remove(4)
    print(mh)
    print(mh.size_)