def solution(n, stations, w):
    answer = 0
    apart = [False for _ in range(n + 1)]
    for station in stations:
        for idx in range(station - w, station + w + 1):
            if 1 <= idx <= n:
                apart[idx] = True
    now = 1
    while now <= n:
        # 전파가 터지는 곳
        if apart[now]:
            now += 1
        # 기지국 설치가 필요한 곳이라면,
        else:
            answer += 1
            now = now + 1 + 2 * w

    return answer

