import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().split() for _ in range(n)] #칭호, 상한값
arr.sort(key=lambda x : int(x[1])) #오름차순
#상한값 배열 입력받기
value = [int(input().strip()) for _ in range(m)]

# 각 상한값마다 칭호 출력
for v in value:
    # 이분탐색
    start, end = 0, len(arr)-1
    answer = 0
    while start<=end:
        mid = (start+end)//2
        if int(arr[mid][1]) >= v: # v보다 크거나 같으면 end을 mid보다 작게 조정
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(arr[answer][0])