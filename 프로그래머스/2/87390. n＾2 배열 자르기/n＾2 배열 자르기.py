def solution(n, left, right):
    answer = []
    # 시간초과 풀이
    # arr = [[i+1]*n for i in range(n)]
    # for i in range(n):
    #     for j in range(i,n):
    #         arr[i][j] = j+1
    #     answer += arr[i]
    # return answer[left:right+1]
    for i in range(left,right+1):
        a = i//n
        b = i%n
        max_v = max(a+1,b+1)
        answer.append(max_v)
    return answer