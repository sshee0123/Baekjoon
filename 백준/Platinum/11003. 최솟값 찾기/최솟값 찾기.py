import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = deque() # (index, value)
for i in range(n):
 while d and d[-1][1] > a[i]: # 덱 맨 뒤 값이 현재 리스트보다 크면 삭제
  d.pop()
 d.append((i, a[i])) # 덱 삭제 된 곳에 삽입
 if d[0][0] <= i-l: # 윈도우 값을 벗어나면
  d.popleft()
 print(d[0][1], end = " ")

