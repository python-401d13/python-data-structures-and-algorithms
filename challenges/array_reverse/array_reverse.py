def reverseArray(arr):
    for i in range(1, len(arr)):
        tmp = arr[i : i + 1]
        if i == len(arr) - 1:
            arr = tmp + arr[:i]
        else:
            arr = tmp + arr[:i] + arr[i + 1 :]
    return arr


print(reverseArray([1, 2, 3]))
