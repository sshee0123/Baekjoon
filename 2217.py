n = int(input())
lope = []
result = []
for i in range(n):
    lope.append(int(input()))
lope.sort(reverse=True)
for i in range(n):
    result.append((i+1)*lope[i])
print(max(result))