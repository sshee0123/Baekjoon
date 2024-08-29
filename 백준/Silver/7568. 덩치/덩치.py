import sys
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    x, y = map(int, input().split())
    answer.append([x,y])

for i in answer:
    rank = 1
    for j in answer:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
    