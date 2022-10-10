def CountingSort(arr):
    n = len(arr)
    arr_new = [0] * len(arr)
    c = [0] * (max(arr)+1)

    for i in range(0, n):
        c[arr[i]] += 1
    # print(c)

    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    # print(c)

    for i in range(len(arr)):
        # arr_new[c[arr[i]]] = arr[i]
        # c[arr[i]] -= 1
        num = arr[i]
        idx = c[num]
        arr_new[idx-1] = num
        c[num] -= 1
    # print(arr_new)

    return arr_new


arr = [1,2,3,4,5,2,4,4,5,3,3,4,5,5,5]
print(CountingSort(arr))