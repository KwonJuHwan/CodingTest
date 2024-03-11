# 문제의 방식 그대로 따라가서 BFS로 구현 -> 로직은 맞지만, 시간 초과
# 열쇠가 될 수 없을 때의 처리가 부족한 것 같음.
# 처음에 회전된 열쇠를 넣어주기
# 그 후, 상하좌우로 이동하면서 자물쇠랑 맞는지 체크
# 맞으면 return 안맞으면 계속해서 이동
# 그러다, 열쇠의 돌기 갯수가 부족하면, 계산

# 자물쇠의 크기를 늘리고, 열쇠를 움직이면서 되는지 확인 -> 열쇠의 크기는 자물쇠보다 무조건 같거나 작으므로, 자물쇠를 3배하여 계산하면 됨
def solution(key, lock):
    def rotate(now_key):
        now_len = len(now_key)
        new_key = [[0 for _ in range(now_len)] for _ in range(now_len)]
        for i in range(now_len):
            now = now_key[i]
            for j in range(now_len):
                new_key[now_len - j - 1][i] = now[j]
        return new_key

    def check(now_lock):
        n = len(now_lock) // 3
        for i in range(n, n * 2):
            for j in range(n, n * 2):
                if now_lock[i][j] != 1:
                    return False
        return True

    n = len(lock)

    # 기존 자물쇠보다 3배 더 큰 자물쇠 초기화
    new_lock = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i + n][j + n] = 1
    # 회전된 열쇠 세팅
    keys = [key, rotate(key), rotate(rotate(key)), rotate(rotate(rotate(key)))]
    # 하나씩 열쇠를 옮겨가며, 자물쇠에 맞는지 체크
    for i in range(1, n * 2):
        for j in range(1, n * 2):
            for k in range(4):
                new_key = keys[k]
                for x in range(len(key)):
                    for y in range(len(key)):
                        new_lock[i + x][j + y] += new_key[x][y]
                if check(new_lock):
                    return True
                # 답이 아니라면, 다시 빼서 그 다음칸 게산
                for x in range(len(key)):
                    for y in range(len(key)):
                        new_lock[i + x][j + y] -= new_key[x][y]
    return False

# from collections import deque
#
#
# def solution(key, lock):
#     answer = True
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     co_i = [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3], [0, 1, 2, 3]]
#     q = deque()
#     # 규격 맞추기
#     start_key = [[0 for _ in range(len(lock))] for _ in range(len(lock))]
#     for i in range(len(key)):
#         for j in range(len(key)):
#             if key[i][j] == 1:
#                 start_key[i][j] = 1
#     # 열쇠의 최소 돌기 개수를 위해, 계산
#     min_lock = 0
#     for i in range(len(lock)):
#         for j in range(len(lock)):
#             if lock[i][j] == 0:
#                 min_lock += 1
#
#     # 회전 함수
#     def rotate(now_key):
#         now_len = len(now_key)
#         new_key = [[0 for _ in range(now_len)] for _ in range(now_len)]
#         for i in range(now_len):
#             now = now_key[i]
#             for j in range(now_len):
#                 new_key[now_len - j - 1][i] = now[j]
#         return new_key
#
#     # 이동 함수
#     def move(now_key, dx, dy):
#         now_len = len(now_key)
#         new_key = [[0 for _ in range(now_len)] for _ in range(now_len)]
#         for i in range(now_len):
#             for j in range(now_len):
#                 if 0 <= i + dx < now_len and 0 <= j + dy < now_len:
#                     new_key[i + dx][j + dy] = now_key[i][j]
#         return new_key
#
#     # 정방향, 90도 회전, 180도 회전, 270도 회전 q에 넣기
#     q.append((start_key, 4))
#     q.append((rotate(start_key), 4))
#     q.append((rotate(rotate(start_key)), 4))
#     q.append((rotate(rotate(rotate(start_key))), 4))
#
#     while q:
#         now_key, now_i = q.popleft()
#         isAnswer = True
#         now_key_hom = 0
#         # 자물쇠랑 열쇠가 맞는지 체크
#         for i in range(len(key)):
#             for j in range(len(key)):
#                 if now_key[i][j] == 1:
#                     now_key_hom += 1
#                 if now_key[i][j] == 0 and lock[i][j] == 0:
#                     isAnswer = False
#                 if lock[i][j] == 1 and now_key[i][j] == 1:
#                     isAnswer = False
#         # 열쇠의 돌기가 자물쇠의 홈보다 개수가 적을 때 -> 방향성이 잘못됨
#         if now_key_hom < min_lock:
#             continue
#         # 열쇠와 자물쇠가 맞음
#         if isAnswer:
#             return isAnswer
#         # 4개의 방향으로 이동 / 갔던 길을 되돌아 가는 거 방지
#         for i in co_i[now_i]:
#             q.append(((move(now_key, dx[i], dy[i])), i))
#     return False
#
# print(solution([[0, 0], [0, 0]],[[1, 0, 0], [1, 0, 0], [1, 1, 1]]))
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
