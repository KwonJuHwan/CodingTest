# 원소 하나의 등수만 구하면 되므로, 굳이 전체의 등수를 매기지 않아도 됨 -> 모든 등수를 처리하려고 하다가 시간초과
# 만약 인센티브를 못받는 직원일 경우는 랭크를 카운팅하지 않고, 넘어가면 되는 부분
# 구하는 것이 전체가 아닌, 부분일 때는 부분에 집중하자.(=부분만 따로 구할 방법이 없는 지 생각)
# 정렬을 최대한 활용 하자!

def solution(scores):
    rank = 1
    target_x, target_y = scores[0][0], scores[0][1]
    target_sum = target_x + target_y

    max_y = 0
    # 이렇게 정렬 했을 때, 탐색 중 앞에 있던 원소들보다 x의 값이 작거나 같음
    # x의 값이 작거나 같으므로, y의 값이 앞에 있던 원소들 중 가장 큰 y값 보다 커야함
    # y값이 더 작지만, x 값이 같을 경우는 y를 오름차 순으로 하였기 때문에, 배제 됨
    # -> y 값이 더 작으면 x 값도 무조건 작음
    scores.sort(key=lambda x: (-x[0], x[1]))

    for x, y in scores:
        if x > target_x and y > target_y:
            return -1

        if y >= max_y:
            # 갱신
            max_y = y
            if x + y > target_sum:
                rank += 1

    return rank

    # import sys


#
#
# def solution(scores):
#     # 원호가 인센티브 못 받을 때,
#     for i in range(1, len(scores)):
#         if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
#             return -1
#     sum_scores = []
#     # 인센티브 받는 인원들만 sum_scores 리스트에 넣기
#     # n**2이 아닌 다른 방법을 찾아야 함
#     cu_scores = []
#     min_x = sys.maxsize
#     min_y = sys.maxsize
#     for i in range(len(scores)):
#         cu_scores.append((scores[i][0], scores[i][1], i))
#         if min_x > scores[i][0]:
#             min_x = scores[i][0]
#         if min_y > scores[i][1]:
#             min_y = scores[i][1]
#
#     x_score = [True for _ in range(len(scores))]
#     cu_scores.sort(key=lambda x: (-x[0], -x[1]))
#     for i in range(len(scores)):
#         stop = False
#         for j in range(i, len(scores)):
#             if cu_scores[i][1] > cu_scores[j][1] and cu_scores[i][0] > cu_scores[j][0]:
#                 x_score[cu_scores[j][2]] = False
#             if cu_scores[i][1] == min_y:
#                 break
#             if cu_scores[i][0] == min_x:
#                 stop = True
#                 break
#         if stop:
#             break
#     for i in range(len(scores)):
#         if x_score[i]:
#             sum_scores.append((scores[i][0] + scores[i][1], i))
#     sum_scores.sort(reverse=True)
#     rank = 1
#     same = 0
#     before = sum_scores[0][0]
#     # 1위일때 예외 처리
#     if sum_scores[0][1] == 0:
#         return 1
#     # 같은 점수를 고려하면서 등수 매기기 + 탐색 중 원호를 만나면 등수 계산 후 바로 return
#     for i in range(1, len(sum_scores)):
#         score = sum_scores[i]
#         if score[1] == 0:
#             if before == score[0]:
#                 return rank
#             else:
#                 return rank + same + 1
#
#         else:
#             if before == score[0]:
#                 same += 1
#             else:
#                 before = score[0]
#                 rank = rank + same + 1
#                 same = 0


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
print(solution([[3, 2], [2, 3], [3, 2], [2, 3]]))
print(solution([[2, 1], [2, 2], [2, 3], [3, 1]]))
print(solution([[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]]))
