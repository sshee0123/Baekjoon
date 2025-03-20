def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    for s in str(age):
        answer += alpha[int(s)]
    return answer