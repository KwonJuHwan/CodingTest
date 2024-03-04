def bfs(places):
    x_1 = [-1, 1, 0, 0]
    y_1 = [0, 0, -1, 1]

    dx = [-2, 0, 2, 0, -1, 1, 1, -1]
    dy = [0, 2, 0, -2, 1, 1, -1, -1]
    cx = [-1, 0, 1, 0, [0, -1], [0, 1], [1, 0], [0, -1]]
    cy = [0, 1, 0, -1, [1, 0], [1, 0], [0, -1], [-1, 0]]
    place = [["s" for _ in range(5)] for _ in range(5)]
    for i in range(5):
        s = places[i]
        for j in range(5):
            place[i][j] = s[j]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                # 거리가 1인 곳 체크
                for l in range(4):
                    if 4 >= i + x_1[l] >= 0 and 4 >= j + y_1[l] >= 0:
                        if place[i + x_1[l]][j + y_1[l]] == "P":
                            return False
                # 거리가 2인 곳 체크
                for k in range(8):
                    if 4 >= i + dx[k] >= 0 and 4 >= j + dy[k] >= 0:
                        if place[i + dx[k]][j + dy[k]] == "P":
                            # 파티션이 없으면 거리두기 X
                            if k >= 4:
                                for x, y in cx[k], cy[k]:
                                    if place[i + x][j + y] != "X":
                                        return False
                            else:
                                if place[i + cx[k]][j + cy[k]] != "X":
                                    return False
                place[i][j] = "X"
    return True


def solution(places):
    answer = []
    for i in range(5):
        if bfs(places[i]):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
