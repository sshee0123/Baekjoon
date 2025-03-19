def solution(array, height):
    answer = [x for x in array if x > height]
    return len(answer)