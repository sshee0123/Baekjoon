import sys
n,c = map(int,sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
#집 오름차순 정렬
house.sort()
start = 1
end = house[-1]-house[0] #집 좌표 차이 최댓값
result = 0
while start<=end:
    mid = (start+end) // 2
    #처음 집부터 공유기 설치
    now = house[0]
    cnt = 1

    for i in range(1,len(house)):
        if house[i] >= now + mid:
            #공유기 설치
            cnt+=1
            now = house[i]
    #공유기 개수가 c가 되어야 한다.
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)