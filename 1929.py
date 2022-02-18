import sys
import math
n, m = map(int,sys.stdin.readline().split())
arr = [True for i in range(m+1)]
for i in range(2,int(math.sqrt(m))+1):
    if arr[i]==True:
        j=2
        while i*j <= m:
            arr[i*j] = False
            j+=1
for i in range(n,m+1):
    if i>1 and arr[i]:
        print(i)
