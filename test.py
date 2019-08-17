class PP():
    def __init__(self):
        pass

    def output(self, str):
        self.length = len(str)
        self.str = str
        self.res = []
        self.temp = []
        self.ff(0)
        return self.res

    def ff(self, start):
        if start == self.length:
            self.res.append(self.temp[:])
            return

        for i in range(start, self.length):
            substr = self.str[start:i+1]
            if substr == substr[::-1]:
                self.temp.append(substr)
                self.ff(i+1)
                self.temp.pop()

s = ""
def helper(array, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid
    return False

arr = [1,3,4,5,6,1,8]
from queue import PriorityQueue
d = PriorityQueue()
for n in arr:
    d.put(n)
while not d.empty():
    print(d.get())
