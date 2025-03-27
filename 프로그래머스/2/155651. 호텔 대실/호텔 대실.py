# def solution(book_time):
#     time_table = [0 for _ in range(60*24)]
#     for s,e in book_time:
#         start = int(s[:2])*60 + int(s[3:])
#         end = int(e[:2])*60 + int(e[3:]) + 10 # 퇴실후 10분 추가
        
#         if end > 60*24 -1:
#             enc = 60*24 -1
#         # 대실 시간 동안 누적합
#         for t in range(start,end):
#             time_table[t] += 1
#     return max(time_table)

def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)