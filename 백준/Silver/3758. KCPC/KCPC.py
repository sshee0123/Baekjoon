import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    #n(팀의개수), k(문제개수), t(당신 팀id), m(로그 엔트리개수)
    n, k, t, m = map(int, input().split())
    score = [[0] * k for _ in range(n)] # 팀별 점수
    submit = [0] * n # 제출횟수
    time = [0] * n # 제출시간
    for log in range(m):
        #i(팀id), j(문제번호), s(획득점수)
        i, j, s = map(int, input().split())
        score[i-1][j-1] = max(score[i-1][j-1], s)
        submit[i-1] += 1
        time[i-1] = log

    # 순위 매기기
    arr = []
    for id in range(n):
        arr.append([sum(score[id]), submit[id], time[id], id+1])
    # 우선순위 : 최종점수 크고, 제출횟수 적고, 제출시간 빠름(적음)
    arr.sort(key=lambda x: (-x[0], x[1], x[2]))
    # print(arr)
    # print(score)
    for r in range(len(arr)):
        if arr[r][3] == t:
            print(r+1)
            break
