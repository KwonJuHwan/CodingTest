import heapq


def solution(jobs):
    k = len(jobs)
    answer = 0
    hq = []
    job = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    now = 0
    while jobs:
        while True and jobs:
            next_start, next_time = jobs.pop(0)
            if next_start <= now:
                heapq.heappush(hq, (next_time, (next_start, next_time)))
            else:
                jobs.insert(0, (next_start, next_time))
                break
        if not hq:
            s_start, s_time = jobs.pop(0)
            now = s_time+s_start
            answer += now - s_start
            continue
        cal, (cal_start, cal_time) = heapq.heappop(hq)
        now += cal_time
        answer += now - cal_start
    while hq:
        calq, (calq_start, calq_time) = heapq.heappop(hq)
        now += calq_time
        answer += now - calq_start
    answer = answer // k
    return answer