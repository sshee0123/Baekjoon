import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr = list(set(arr))
arr.sort()
for i in arr:
    print(i,end=' ')