import sys
N = int(input())
card = list(map(int,sys.stdin.readline().split()))
M = int(input())
check = list(map(int,sys.stdin.readline().split()))
card.sort()

def binary_search(target,arr):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if card[mid] == target:
            return 1
        elif card[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

for i in check:
    print(binary_search(i,card),end=' ')
