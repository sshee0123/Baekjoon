import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
c = [0] * m
answer = 0
# 합 배열
s[0] = a[0]
for i in range(1,n):
    s[i] = s[i-1]+a[i]

# 나머지 배열
for i in range(n):
    remainder = s[i]%m
    if remainder == 0:
        answer += 1
    c[remainder] += 1

# 나머지 배열 조합 구하기
for i in range(m):
    if c[i] > 1: # 나머지가 있을때,
        answer += ((c[i])*(c[i]-1))//2
print(answer)