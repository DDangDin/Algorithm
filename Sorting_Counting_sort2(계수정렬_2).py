def CountingSort(arr):
    arr_new = [0] * len(arr)
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for num in arr:
        idx = count[num]
        arr_new[idx-1] = num
        count[num] -= 1


arr = [1,2,3,4,5,2,4,4,5,3,3,4,5,5,5]
CountingSort(arr)