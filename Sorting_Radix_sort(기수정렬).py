def RadixSort(arr):
    maxNum = max(arr)
    digit = 1

    def CountingSort(arr, digit):
        arr_new = [0] * len(arr)
        count = [0] * (10)  # 자릿수 당 숫자는 0~9 (10자리)

        for num in arr:
            idx = num//digit
            count[idx%10] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for num in range(len(arr)-1, -1, -1):
            tmp = (arr[num]//digit)%10
            idx = count[tmp]
            arr_new[idx-1] = arr[num]
            count[tmp] -= 1
        
        for i in range(len(arr)): 
            arr[i] = arr_new[i]
        
        return arr

    while maxNum//digit > 0:
        result = CountingSort(arr, digit)
        digit *= 10
    
    return result
        

arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
print(RadixSort(arr))