n = int(input())
data = list(map(int,input().split()))
arr = []

for i in range(n-1):
    cnt = 0
    for j in range(i+1,n):
        if data[i]>data[j]:
            cnt+=1
        else:
            break
    arr.append(cnt)
print(max(arr))
