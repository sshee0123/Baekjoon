import sys

a,b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

m = b+c
while m>=60:
    a+=1
    m-=60
    if a>=24:
        a = 0
print(a,m)
