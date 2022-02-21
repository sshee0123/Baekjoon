import sys
from itertools import combinations

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    k = arr[0]
    if k == 0: #종료조건
        break
    s = arr[1:]

    #조합
    n = list(combinations(s,6))
    # print(n)
    for i in n:
        for j in i:
            print(j,end=" ")
        print()
    print()


