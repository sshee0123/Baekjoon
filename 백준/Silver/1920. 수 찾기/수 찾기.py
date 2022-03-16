import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
A.sort()

M = int(input())
B = list(map(int,sys.stdin.readline().split()))

def binary_search(target,arr):
    # arr.sort()
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

for i in B:
    print(binary_search(i,A))