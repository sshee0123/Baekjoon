import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

#중복 제거 후 sort
set_arr = list(set(arr))
set_arr.sort()
set_arr.sort(key = len)
for i in set_arr:
    print(i)

