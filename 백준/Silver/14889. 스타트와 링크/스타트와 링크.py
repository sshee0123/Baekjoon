from itertools import combinations

n= int(input())
p = [list(map(int,input().split())) for _ in range(n)]

members = [i for i in range(n)]
cases = list(combinations(members,n//2))

min_value = 1e9
for case in cases:
    start = 0
    link = 0
    for x in case:
        for y in case:
            start += p[x][y]
    other_case = [x for x in range(n) if x not in case]
    for x in other_case:
        for y in other_case:
            link += p[x][y]
    min_value = min(min_value,abs(start-link))
print(min_value)