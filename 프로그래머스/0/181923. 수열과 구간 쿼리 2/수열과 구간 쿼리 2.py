def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        tmp = []
        for i in range(s,e+1):
            if arr[i] > k:
                tmp.append(arr[i])
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
    return answer