import sys
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

s = set(arr)
if len(s) == 1:
    print(10000 + arr[0]*1000)
elif len(s) == 3:
    print(arr[-1]*100)
else:
    print(1000+arr[1]*100)