def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid  # return index
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1



arr = [1,2,3,4,5,6]
target = 5  # index -> 2
target_index = BinarySearch(arr, target)
print("array: ", arr)
print("target: ", target)
print("findIndex: ", target_index)