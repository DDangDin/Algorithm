# 리스트 slice를 할 때 배열의 복제가 일어나므로 메모리 사용 효율은 좋지 않음
def MergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = MergeSort(arr[:mid])
    high_arr = MergeSort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(MergeSort(arr))