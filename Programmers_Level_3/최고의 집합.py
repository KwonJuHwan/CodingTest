def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    min_s = s // n
    ss = [min_s for _ in range(n)]
    remain_s = s - min_s * n

    for i in range(remain_s):
        ss[i] += 1
    ss.sort()
    answer = ss

    return answer
