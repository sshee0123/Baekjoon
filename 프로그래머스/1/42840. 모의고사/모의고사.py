def solution(answers):
    answer = []
    score = [0]*3 # 수포자 점수
    # 수포자 찍기 규칙
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for i, ans in enumerate(answers):
        if p1[i%len(p1)] == ans:
            score[0] += 1
        if p2[i%len(p2)] == ans:
            score[1] += 1
        if p3[i%len(p3)] == ans:
            score[2] += 1
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    return answer