import sys
from collections import deque


def solution(board):
    n = len(board[0]) - 1
    dp = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = int(1e9)
    q = deque()
    # x, y , 방향, cost 
    q.append((0, 0, 5, 0))
    while q:
        pop = q.popleft()
        cost = pop[3]
        if (pop[0], pop[1]) == (n, n) and answer > cost:
            answer = cost
        for i in range(4):
            x = pop[0] + dx[i]
            y = pop[1] + dy[i]
            if 0 <= x <= n and 0 <= y <= n:
                if board[x][y] != 1:
                    add_cost = 600 if pop[2] != i else 100
                    if dp[x][y] >= cost + add_cost - 400:
                        dp[x][y] = cost + add_cost
                        q.append((x, y, i, cost + add_cost))
    #
    # for i in range(n + 1):
    #     print(board[i])
    return answer-500


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 0]]))
