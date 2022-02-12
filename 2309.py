import sys
arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))
sum_arr = sum(arr)
m1 = 0
m2 = 0

for i in range(8):
    for j in range(i+1,9):
        if sum_arr-(arr[i]+arr[j]) ==100:
            m1 = arr[i]
            m2 = arr[j]
arr.remove(m1)
arr.remove(m2)
arr.sort()
for i in arr:
    print(i)