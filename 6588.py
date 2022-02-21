import sys
import math

arr = [True for _ in range(1000001)]
for i in range(2,int(math.sqrt(1000001))):
    if arr[i]:
        j = 2
        while i*j<1000001:
            arr[i*j] = 0
            j+=1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    flag = 0
    for i in range(3,len(arr)):
        if arr[i]:
            if arr[n-i]:
                print(n, "=", i, "+", n-i)
                flag = 1
                break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
