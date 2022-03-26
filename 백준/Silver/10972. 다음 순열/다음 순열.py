# 10972
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
x = 0
for i in range(n-1, 0, -1):
    if arr[i] > arr[i-1]:
        x = i-1
        break
for i in range(n-1, 0, -1):
    if arr[x] < arr[i]:
        arr[x], arr[i] = arr[i], arr[x]
        arr = arr[:x+1] + sorted(arr[x+1:])
        print(*arr)
        exit()
print(-1)
