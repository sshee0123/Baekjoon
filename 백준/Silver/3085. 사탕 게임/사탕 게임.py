# 3085

import sys
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
answer = 0

# 완전 탐색
def check(array):
    max_len = 1 # 함수의 리턴 값 -> 가장 긴 최대 길이
    for i in range(n):
        # 열 비교
        cnt = 1 # 같은 색인 최대 길이
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else: # 인접한 사탕 중 다른 색 나오면 cnt 초기화
                cnt = 1
            max_len = max(max_len, cnt) # max_len 갱신
        
        # 행 비교
        cnt = 1  # 같은 색인 최대 길이
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_len = max(max_len, cnt)  # max_len 갱신
    return max_len

# 인접하고 색 다른 두 칸 고르고 완탐 호출
for i in range(n):
    for j in range(n):
        if j+1<n: # 인접한 열 끼리 비교 후 교체
            if arr[i][j] != arr[i][j+1]:
                arr[i][j],arr[i][j+1] = arr[i][j+1], arr[i][j]
                # 완전탐색 수행
                tmp = check(arr)
                # 정답과 완탐 CNT 비교
                answer = max(answer,tmp)
                # 교체 한 것 다시 원래대로 돌려놓기 ( 모든 경우의수 비교해야함)
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i+1<n: # 인접한 행 끼리 비교 후 교체
            if arr[i][j] != arr[i+1][j]:
                arr[i][j], arr[i + 1][j] = arr[i + 1][j],arr[i][j]
                # 완전탐색 수행
                tmp = check(arr)
                # 정답과 완탐 CNT 비교
                answer = max(answer, tmp)
                # 교체 한 것 다시 원래대로 돌려놓기 ( 모든 경우의수 비교해야함)
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
print(answer)