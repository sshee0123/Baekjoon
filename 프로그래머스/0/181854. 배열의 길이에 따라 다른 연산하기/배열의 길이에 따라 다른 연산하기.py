def solution(arr, n):
    answer = []
    arr_len = len(arr)
    if arr_len %2 == 0:
        for i in range(1,arr_len,2):
            arr[i] = arr[i]+n
    else:
        for i in range(0,arr_len+1,2):
            arr[i] = arr[i]+n
    return arr 