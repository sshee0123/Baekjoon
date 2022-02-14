import sys
n = int(input())
arr = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    arr.append([x,y])
arr.sort(key = lambda a: (a[1],a[0]) )
for x,y in arr:
    print(x,y)
