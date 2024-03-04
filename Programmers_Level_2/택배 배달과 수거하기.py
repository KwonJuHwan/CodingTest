def solution(cap, n, deliveries, pickups):
    d_stack = []
    p_stack = []
    i = 1
    for delivery in deliveries:
        if delivery != 0:
            d_stack.append((i, delivery))
        i += 1
    i = 1
    for pickup in pickups:
        if pickup != 0:
            p_stack.append((i, pickup))
        i += 1
    answer = 0
    while True:
        max_len = 0
        now = 0
        while len(d_stack) > 0:
            d_pop = d_stack.pop()
            max_len = max(max_len, d_pop[0])
            if now + d_pop[1] > cap:
                d_stack.append((d_pop[0], d_pop[1] - (cap - now)))
                break
            elif now + d_pop[1] == cap:
                break
            else:
                now += d_pop[1]
        now = 0
        while len(p_stack) > 0:
            p_pop = p_stack.pop()
            max_len = max(max_len, p_pop[0])
            if now + p_pop[1] > cap:
                p_stack.append((p_pop[0], p_pop[1] - (cap - now)))
                break
            elif now + p_pop[1] == cap:
                break
            else:
                now += p_pop[1]
        answer += max_len * 2
        if len(d_stack) == 0 and len(p_stack) == 0:
            break
    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
