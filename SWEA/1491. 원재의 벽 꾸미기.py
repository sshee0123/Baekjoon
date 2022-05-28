T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, A, B = map(int,input().split())
    answer = -1
    for r in range(1,N+1):
        c = 1
        while r*c <= N:
            cond = A * abs(r-c) + B*(N-r*c)
            if answer == -1:
                answer = cond
            else:
                answer = min(answer, cond)
            c += 1
    print("#%d %d" %(test_case, answer))
출처: https://10000say-gabozago.tistory.com/193 [가보자고:티스토리]
