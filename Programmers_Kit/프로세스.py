from collections import defaultdict, deque


def solution(priorities, location):
    answer = 0
    que = deque()
    dict = defaultdict(int)
    se = []
    for i in range(len(priorities)):
        que.append((i, priorities[i]))
        dict[priorities[i]] += 1
    for i in dict.keys():
        se.append((i, dict.get(i)))
    se.sort(key=lambda x: -x[0])
    k = 0
    out_prior = se[k][0]
    out_sum = se[k][1]
    while que:
        index, prior = que.popleft()
        if out_prior == prior:
            answer += 1
            if location == index:
                break
            out_sum -= 1
        else:
            que.append((index, prior))
        if out_sum == 0:
            k += 1
            out_prior = se[k][0]
            out_sum = se[k][1]

    return answer