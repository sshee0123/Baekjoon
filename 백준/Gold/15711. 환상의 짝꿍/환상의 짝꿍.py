#15711
import sys
import math
t = int(sys.stdin.readline())

#에라토스테네스의 체
# n = 2*(10**12) #메모리초과
n = 2*(10**6) + 1
arr = [False,False] + [True for i in range(n-1)]
prime = []
# for i in range(2,int(math.sqrt(n))+1):
for i in range(2,n):
    if arr[i]:
        prime.append(i)
        for j in range(i+i, n, i):
            arr[j] = False

def isPrime(num):
    if num > n:
        for p in prime:
            if p >= num:
                break
            if num % p == 0:
                return False
        return True
    else:
        return arr[num]

for _ in range(t):
    ab = sum(map(int,sys.stdin.readline().split()))
    if ab<4:
        print("NO")
    elif ab % 2 == 0:
            print("YES")
    else:
        if isPrime(ab-2):
            print("YES")
        else:
            print("NO")