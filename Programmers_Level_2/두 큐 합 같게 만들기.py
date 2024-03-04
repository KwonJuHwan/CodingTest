from collections import deque


def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    answer = 0
    sum1 = sum(que1)
    sum2 = sum(que2)
    while sum1 != sum2:
        if sum1 > sum2:
            popleft = que1.popleft()
            que2.append(popleft)
            sum1 -= popleft
            sum2 += popleft
            answer += 1
        else:
            popleft = que2.popleft()
            que1.append(popleft)
            answer += 1
            sum2 -= popleft
            sum1 += popleft
        if len(que1) == 0 or len(que2) == 0:
            answer = -1
            break
        if answer >= 600000:
            answer = -1
            break

    return answer


print(solution([1, 2, 4], [3, 2, 4]))
