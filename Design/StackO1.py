class SpecialStack:
    """Design a special stack to implement getMin() in Time O(1); Space O(1)"""
    def __init__(self):
        self.data = []
        self.minv = None

    def push(self, x):
        if self.data:
            if x >= self.minv:
                self.data.append(x)
            else:
                self.data.append(2 * x - self.minv)
                self.minv = x
        else:
            self.data.append(x)
            self.minv = x

    def pop(self):
        if not self.data:
            # self.minv = None
            return None
        y = self.data.pop()
        if y < self.minv:
            ori_item = self.minv
            self.minv = 2 * self.minv - y
            return ori_item
        return y

    def get_min(self):
        if self.data:
            return self.minv
        return None



class SpecialStack_N:
    """Time O(1); Space O(n)"""
    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, x):
        if (not self.min_data) or self.min_data[-1] >= x:
            self.min_data.append(x)
        self.data.append(x)

    def pop(self):
        if not self.data:
            return None
        pop_item = self.data.pop()
        if self.min_data[-1] == pop_item:
            self.min_data.pop()
        return pop_item

    def get_min(self):
        if self.min_data:
            return self.min_data[-1]
        return None


if __name__ == '__main__':
    push_items = [3,2,2,4,2,1,5]
    ss = SpecialStack()
    for x in push_items:
        ss.push(x)
    print('Initial: {}'.format(ss.data))

    while True:
        print('min value: {}'.format(ss.get_min()))
        pop_item = ss.pop()
        print('pop: {}, data: {}'.format(pop_item, ss.data))
        print()
        if pop_item is None:
            break
