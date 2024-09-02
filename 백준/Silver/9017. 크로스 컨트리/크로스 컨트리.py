import sys
from collections import Counter
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    score_list = list(map(int, input().split()))
    participation = []
    counter = Counter(score_list)
    #print("counter" , counter)
    for k, v in counter.items():
        if v == 6:
            participation.append(k)
    #print("participation" , participation)

    score = {}
    rank = 1
    for i in range(n):
        if score_list[i] in participation:
            if score_list[i] in score: # 있으면 추가
                score[score_list[i]].append(rank)
            else: # 없으면 새로
                score[score_list[i]] = [rank]
            rank += 1
    #print("score", score)
    myscore = sorted(score.items(), key=lambda x:(sum(x[1][:4]), x[1][4], x[1][5]))
    print(myscore[0][0])

