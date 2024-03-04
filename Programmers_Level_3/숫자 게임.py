from collections import deque


def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    qA = deque(A)
    qB = deque(B)

    for i in range(len(A)):
        minA = qA.pop()
        minB = qB.pop()
        # B가 승점 획득을 할 수 없음
        if minB <= minA:
            qA.append(minA)
            qA.popleft()
        else:
            answer += 1

    return answer
