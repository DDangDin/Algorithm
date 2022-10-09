# 삽입정렬 (Insertion sort)

arr = [6,5,3,1,8,7,2,4]

n = len(arr)

for i in range(1, n):
  for j in range(i, 0, - 1):
    if arr[j-1] > arr[j]:
      arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr)