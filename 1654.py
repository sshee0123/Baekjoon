import sys
k,n = map(int,sys.stdin.readline().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)
#μ΄λΆνμ
while (start<=end):
    total = 0
    mid = (start+end)//2
    for i in arr:
        total += i//mid
    if total >= n:
        start = mid + 1
    else:
        end = mid -1

print(end)
