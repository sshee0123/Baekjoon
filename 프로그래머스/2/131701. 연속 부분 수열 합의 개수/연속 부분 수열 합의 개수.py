def solution(elements):
    answer = []
    n = len(elements)
    elements = elements*2
    for i in range(n):
        for j in range(n):
            answer.append(sum(elements[j:j+i+1]))
    return len(set(answer))