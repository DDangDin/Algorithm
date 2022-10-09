def SequentialSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # return (array)index

arr = [1,2,3,4,5,6]
target = 3  # index -> 2
target_index = SequentialSearch(arr, target)
print("array: ", arr)
print("target: ", target)
print("findIndex: ", target_index)