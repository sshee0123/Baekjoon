import sys

T = int(input())
for i in range(T):
    people = []
    n = int(input())
    for j in range(n):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper,interview])
    people.sort()
    good_interview = people[0][1]
    cnt = 1

    for z in range(1,n):
        if people[z][1]<good_interview:
            good_interview = people[z][1]
            cnt+=1

    print(cnt)