n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
s = sorted(arr)
for x,y in s:
    print(x,y)