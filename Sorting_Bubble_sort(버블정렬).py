# 버블 정렬(bubble sort)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(len(arr))

for i in range(len(arr)-1):
  for j in range(len(arr)-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)