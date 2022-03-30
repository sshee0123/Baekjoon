import sys

a, b = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = []
for i in arr:
    if i < b:
        result.append(i)
for r in result:
    print(r,end=" ")