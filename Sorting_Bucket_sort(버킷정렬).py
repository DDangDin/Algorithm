def BucketSort(arr):
    bucket = []

    size = len(arr)
    for i in range(size):
        bucket.append([])
    # print(bucket)

    for i in arr:
        index = i * size // (max(arr) + 1) 
        bucket[index].append(i)
    # print(bucket)

    for i in range(size):
        bucket[i] = sorted(bucket[i])
    # print(bucket)

    k=0
    for i in range(size):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 15]
print(BucketSort(arr))