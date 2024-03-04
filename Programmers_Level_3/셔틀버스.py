def solution(n, t, m, timetable):
    answer = ''
    table = [0 for _ in range(len(timetable))]
    
    for i, time in enumerate(timetable):
        table[i] = int(time[0:2]) * 60 + int(time[3:5])

    table.sort()
    bus_time = [0 for _ in range(n)]
    bus = [[] for _ in range(n)]

    now_time = 540
    bus_time[0] = now_time
    # 버스 도착 시간표 만들기
    if n > 1:
        for i in range(1, n):
            bus_time[i] = now_time + t * i

    crew = 0
    # 순서 대로 버스 타는 로직
    for i in range(n):
        now_time = bus_time[i]
        # 현재 인원 수
        size = 0
        while size < m:
            if table[crew] <= now_time:
                bus[i].append(table[crew])
                crew += 1
                size += 1
            else:
                break
            if crew == len(table):
                break
        if crew == len(table):
            break

    # 빈 자리가 없을 때,
    if len(bus[n - 1]) == m:
        last = bus[n - 1].pop() - 1
    # 빈 자리가 있을 때,
    else:
        last = bus_time[n - 1]

    # 시간 계산
    h = last // 60
    m = last % 60
    if h < 10:
        if m < 10:
            answer = "0"+str(h)+":0"+str(m)
        else:
            answer = "0"+str(h)+":"+str(m)
    else:
        if m < 10:
            answer = str(h)+":0"+str(m)
        else:
            answer = str(h)+":"+str(m)

    return answer


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
