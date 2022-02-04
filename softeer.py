import sys
import bisect


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

answer = [] # 앞에서부터 확인한 돌의 높이
answer_rev = [] # 뒤에서부터 확인한 돌의 높이
high_target = [1] * n # 앞에서부터 밟은 돌의 개수
low_target = [1] * n # 뒤에서부터 밟은 돌의 개수

# 반복문을 통해 돌의 높이를 확인
for i in range(n):

    # ------- 앞에 돌부터 확인 ---------

    # 확인한 돌이 없으면 현재 돌의 높이를 리스트에 추가
    if len(answer) == 0:
        answer.append(a[i])
    else:
        # 현재 돌의 높이가 리스트에 마지막 돌보다 높으면
        if a[i] > answer[-1]:
            # 리스트에 추가
            answer.append(a[i])
        else:
            # 리스트에 마지막 돌이 더 높으면
            # 리스트에 현재 돌의 위치 인덱스에 현재 돌의 높이로 초기화 시킨다.
            index = bisect.bisect_left(answer, a[i])
            answer[index] = a[i]

    # ------- 뒤에 돌부터 확인 ---------

    # 뒤에 돌부터 확인하기 때문에 i가 아닌 n - 1 - i로 돌의 높이를 확인한다.
    # 확인한 돌이 없으면 현재 돌의 높이를 리스트에 추가
    if len(answer_rev) == 0:
        answer_rev.append(a[n - 1 - i])
    else:
        # 현재 돌의 높이가 리스트에 마지막 돌보다 높으면
        if a[n - 1 - i] > answer_rev[-1]:
            # 리스트에 추가
            answer_rev.append(a[n - 1 - i])
        else:
            # 리스트에 마지막 돌이 더 높으면
            # 리스트에 현재 돌의 위치 인덱스에 현재 돌의 높이로 초기화 시킨다.
            index = bisect.bisect_left(answer_rev, a[n - 1 - i])
            answer_rev[index] = a[n - 1 - i]

    # 확인한 돌의 높이의 개수를 리스트에 추가한다.
    high_target[i] = len(answer)
    low_target[n - 1 - i] = len(answer_rev)


result_target = [0] * n

# 반복문을 통해 돌을 밟은 개수를 더한다.
for i in range(n):
    result_target[i] = high_target[i] + low_target[i]

# 돌을 밟은 개수의 최대 값에서 1 빼준 값을 출력
# 최대 값에서 두번 돌을 밟기 때문에 1을 빼준다.
print(max(result_target) - 1)