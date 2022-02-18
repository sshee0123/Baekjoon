import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
if n==1:
    print(arr[0]*arr[0])
else:
    print(max(arr)*min(arr))