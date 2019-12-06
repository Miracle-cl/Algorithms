def heapify(i, n, arr):
    largest = i
    ll = 2 * i + 1
    rr = 2 * i + 2
    if ll < n and arr[largest] < arr[ll]:
        largest = ll
    if rr < n and arr[largest] < arr[rr]:
        largest = rr
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(largest, n, arr)
        


def heap_sort(arr):
    n = len(arr)
    # build max heap
    for i in range(n//2-1, -1, -1):
        heapify(i, n, arr)
    
    # extract max element and put last location
    for i in range(n-1, 0, -1):
        # print(i)
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i, arr)
    return arr


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    res = heap_sort(arr)
    print(res)