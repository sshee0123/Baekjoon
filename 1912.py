import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
d = [arr[0]]
for i in range(0,n-1):
    d.append(max(d[i]+arr[i+1], arr[i+1]))
print(max(d))