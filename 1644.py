import sys
import math
n = int(sys.stdin.readline())
arr = [False]+[True]*(n)
prime_num = []
for i in range(2,int(math.sqrt(n))+1):
    if arr[i]:
        for j in range(i*2,n+1,i):
            arr[j]=False
for i in range(2,n+1):
    if arr[i]:
        prime_num.append(i)

result = 0
start = 0
end = 0

while end<=len(prime_num):
    tmp = sum(prime_num[start:end])
    if tmp == n:
        result+=1
        end+=1
    elif tmp<n:
        end+=1
    else:
        start+=1
print(result)