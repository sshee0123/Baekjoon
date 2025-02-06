def solution(num_str):
    # answer = 0
    # for i in num_str:
    #     answer += int(i)
    
    answer = sum([int(i) for i in num_str])
    return answer