def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i, j, k = commands[c]
        tmp = []
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer