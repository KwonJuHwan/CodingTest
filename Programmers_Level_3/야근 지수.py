import heapq


def solution(n, works):
    answer = 0
    q = []
    for work in works:
        heapq.heappush(q, -work)

    for i in range(n):
        if not q:
            break
        pop = heapq.heappop(q)
        # 일 잔량이 남아 있으면
        if pop < -1:
            heapq.heappush(q, pop + 1)
    # 일이 남아있으면
    if q:
        for w in q:
            answer += pow(w, 2)
    return answer


print(solution(4, [4, 3, 3]))
