import sys
input = sys.stdin.readline
n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
s = [] # 스택에 index 삽입

for i in range(n):
    while s and a[s[-1]] < a[i]: # 스택 top 보다 스택에 들어올 수가 더 크면 오큰수
        ans[s.pop()] = a[i] # 스택에서 빼면서 정답에 오큰수 삽입
    s.append(i) # 오큰수 아니면 index 삽입
# 오큰수 없는 값 -1 처리
while s:
    ans[s.pop()] = -1
# 정답 출력
for i in range(n):
    sys.stdout.write(str(ans[i])+" ")
