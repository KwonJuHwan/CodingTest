def solution(rows, columns, queries):
    answer = []
    maps = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    n = 1
    # 초기 세팅
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            maps[i][j] = n
            n += 1
    dx = [0, 0, 0, 0]
    dy = [0, 0, 0, 0]
    for i in range(len(queries)):
        dx[0], dx[1], dx[2], dx[3] = queries[i][0], queries[i][0], queries[i][2], queries[i][2]
        dy[0], dy[1], dy[2], dy[3] = queries[i][1], queries[i][3], queries[i][3], queries[i][1]
        x, y = dx[0], dy[0]
        first = maps[x][y]
        min_score = maps[x][y]
        before_score = first
        while y != dy[1]:
            # print("before: ", before_score, "temp: ", maps[x][y + 1])
            temp = maps[x][y + 1]
            maps[x][y + 1] = before_score
            before_score = temp
            min_score = min(min_score, temp)
            y += 1
        while x != dx[2]:
            # print("before: ", before_score, "temp: ", maps[x+1][y])
            temp = maps[x + 1][y]
            maps[x + 1][y] = before_score
            before_score = temp
            min_score = min(min_score, temp)
            x += 1
        while y != dy[3]:
            # print("before: ", before_score, "temp: ", maps[x][y - 1])
            temp = maps[x][y - 1]
            maps[x][y - 1] = before_score
            before_score = temp
            min_score = min(min_score, temp)
            y -= 1
        while x != dx[0]:
            # print("before: ", before_score, "temp: ", maps[x - 1][y])
            temp = maps[x - 1][y]
            maps[x - 1][y] = before_score
            before_score = temp
            min_score = min(min_score, temp)
            x -= 1
        answer.append(min_score)
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
