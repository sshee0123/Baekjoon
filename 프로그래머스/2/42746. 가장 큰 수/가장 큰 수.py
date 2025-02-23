def solution(numbers):
    # 문자열로 바꿔주고
    numbers = list(map(str, numbers))
    # 문자열 3번씩 반복 (numbers의 원소의 길이는 0이상 1000이하이기때문)
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))