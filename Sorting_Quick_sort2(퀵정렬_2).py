def QuickSort(arr):
    
    def sort(arr, start, end):
        if start >= end:
            return

        pivot = start
        left = start + 1
        right = end

        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                right -= 1
            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        sort(arr, start, right - 1)
        sort(arr, right + 1, end)

    sort(arr, 0, len(arr)-1)
    return arr

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = QuickSort(arr)
print(result)