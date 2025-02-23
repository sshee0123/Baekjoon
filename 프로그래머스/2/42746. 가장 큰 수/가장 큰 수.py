from functools import cmp_to_key
def compare(x,y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
        return 1
def solution(numbers):
    answer = ''
    numbers = [str(x) for x in numbers]
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = str(''.join(numbers))
    # numbers가 모두 0인 경우 (예외상황)
    if answer=='0'*len(numbers):
        return '0'
    else:
        print("0아님")
        return answer