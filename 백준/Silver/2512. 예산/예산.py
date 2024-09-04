import sys
input = sys.stdin.readline

#이분탐색
n = int(input())
asking = list(map(int, input().split()))
m = int(input()) #예산
s, e = 1, max(asking)
answer = 0
while s<=e:
    mid = (s+e)//2 #상한액 정하기
    tmp = 0 #예산 합
    for i in asking:
        if i > mid:
            tmp += mid
        else:
            tmp += i

    if tmp > m:
        e = mid-1
    else:
        s = mid +1
        answer = mid
print(answer)