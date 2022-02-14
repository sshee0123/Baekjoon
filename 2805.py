import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
# trees.sort()
start = 0
end = max(trees)

while start<=end:
    log = 0
    mid = (start+end)//2
    for i in trees:
        if i >= mid:
            log+=i-mid
    if log >= M:
        start = mid+1
    else:
        end = mid-1
print(end)