class MergeSort():
    def __init__(self, arr):
        self.arr = arr

    def merge_array(self, left, mid, right):
        temp = []
        i = left
        j = mid
        while i < mid and j < right:
            if self.arr[i] < self.arr[j]:
                temp.append(self.arr[i])
                i += 1
            else:
                temp.append(self.arr[j])
                j += 1
        while i < mid:
            temp.append(self.arr[i])
            i += 1
        while j < right:
            temp.append(self.arr[j])
            j += 1
        assert right - left == len(temp)
        self.arr[left:right] = temp
        # for i in range(len(temp)):
        #     self.arr[left + i] = temp[i]

    def merge_sort(self, left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        self.merge_sort(left, mid)
        self.merge_sort(mid, right)
        self.merge_array(left, mid, right)

arr = [4,5,2,4,1,8,9,0]
ms = MergeSort(arr)
ms.merge_sort(0, len(arr))
print(ms.arr)
