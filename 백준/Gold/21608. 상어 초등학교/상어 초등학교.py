from collections import defaultdict

n = int(input())
class_=[[0]*n for _ in range(n)]
likedict = defaultdict(list)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = 0

for _ in range(n*n):
    input_list = list(map(int,input().split()))
    likedict[input_list[0]] = input_list[1:] #학생과 좋아하는 학생들 dict에 넣기
    max_x = 0
    max_y = 0
    max_like = -1
    max_blank = -1
    
    for i in range(n):
        for j in range(n):
            if class_[i][j] == 0: #빈칸이면
                #dfs
                likecnt = 0
                blankcnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if class_[nx][ny] in input_list: #좋아하는 리스트
                            likecnt+=1
                        if class_[nx][ny] ==0: #빈칸
                            blankcnt+=1
                if max_like<likecnt or (max_like ==likecnt and max_blank < blankcnt):
                    max_like = likecnt
                    max_blank = blankcnt
                    max_x = i
                    max_y = j
    class_[max_x][max_y] = input_list[0]
#만족도
for i in range(n):
    for j in range(n):
        cnt = 0
        like = likedict[class_[i][j]] #좋아하는 사람들
        #사방 조사 dfs
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if class_[nx][ny] in like:  #좋아하는사람들이 사방에 있으면
                    cnt+=1
        #0:0 1:1 2:10 3:100 4:1000
        if cnt!=0:
            result +=10**(cnt-1)
print(result)
            