import sys
input = sys.stdin.readline
arr = list(input().strip())
n = 0
while len(arr):
    n += 1
    num = str(n)
    # print("num",num)
    # print("arr[0]", arr[0])
    while len(num) and len(arr):
        if num[0] == arr[0]: #자리수
            arr = arr[1:]
        num = num[1:]
print(n)
