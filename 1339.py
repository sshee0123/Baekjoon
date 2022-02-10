n = int(input())
arr = []
alpha_dict = {}
value_list = []
for i in range(n):
    arr.append(input())
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] not in alpha_dict:
            alpha_dict[arr[i][j]] = 10**(len(arr[i])-j-1)
        else:
            alpha_dict[arr[i][j]] += 10**(len(arr[i])-j-1)
for v in alpha_dict.values():
    value_list.append(v)
value_list.sort(reverse=True)

#9부터 1까지 곱해주기
sum = 0
start = 9
for i in value_list:
    sum+=i*start
    start-=1
print(sum)

