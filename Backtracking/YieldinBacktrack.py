def perm(arr, pos = 0):
    if pos == len(arr):
        yield arr
    for i in range(pos, len(arr)):
        arr[pos], arr[i] = arr[i], arr[pos]
        for _ in perm(arr, pos + 1): 
            yield _
        arr[pos], arr[i] = arr[i], arr[pos]


x = perm([1,2,3,4])
# next(x)
for _ in x:
    print(_)