import sys

def solution(index):
    for i in range(1,index//2+1):
        if arr[-i:] == arr[-i*2:-i]:
            return -1
    if index == n:
        for i in range(n):
            print(arr[i],end="")
        return 0

    for i in range(1,4):
        arr.append(i)
        if solution(index+1)==0:
            return 0
        arr.pop()

n = int(sys.stdin.readline())
arr = []
solution(0)
