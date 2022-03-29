import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    arr = ''
    arr += ' '*(n-i)
    arr += '*'*i
    print(arr)