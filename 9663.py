import sys
n = int(sys.stdin.readline())
chess = [0] * n
cnt = 0

def possible(x):
    for i in range(x):
        #행 돌면서
        #상하좌우 or 대각선에 퀸이 있다면 False 반환
        #여기서 대각선은 행-행 = 열-열
        if chess[x] == chess[i] or abs(chess[x]-chess[i]) == abs(x-i):
            return False
    return True

def solution(x):
    global cnt
    #재귀로 x가 계속 +1 되는데 x가 n이 되면 경우의 수 +1
    if x==n:
        cnt+=1
    else:
        for i in range(n):
            #chess판의 (x,i)에 퀸을 놓는다.
            chess[x] = i
            if possible(x):
                #퀸이 상하좌우, 대각선으로 공격할 수 없다면 다음 퀸 놓기
                solution(x+1)

solution(0)
print(cnt)