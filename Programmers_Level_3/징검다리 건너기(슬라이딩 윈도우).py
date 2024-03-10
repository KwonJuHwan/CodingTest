# 구역을 나눠서 계산 -> 시간초과
# import sys
# def solution(stones, k):
#     answer = sys.maxsize
#     for i in range(len(stones) - (k - 1)):
#         answer = min(answer, max(stones[i:i + k]))
#     return answer

# 슬라이딩 윈도우 개념을 생각하여, 계산 -> 한개 문항 시간 초과
# from collections import deque
# def solution(stones, k):
#     now = [stones[i] for i in range(k)]
#     q = deque(now)
#     max_now = max(now)
#     answer = max_now
#     for i in range(k,len(stones)):
#         if max_now == q.popleft():
#             max_now = max(q)
#         q.append(stones[i])
#         if stones[i] > max_now:
#             max_now = stones[i]
#         answer = min(answer,max_now)
#     return answer

# 불필요한 계산을 줄인 슬라이딩 + heap -> 통과
# 슬라이딩 윈도우 개념 + 필요없는 게산은 하지 않는 것
# 여기서 필요없는 계산이란, 범위가 달라지면 계속해서 최댓값을 업데이트 해주는 것이 아닌
# 최대인 값의 인덱스가 현재 상황에서 삭제되어야 하는 값이라면, 삭제 후, 최댓값 갱신(heap을 이용하여 갱신)
# 빼고, 더한 값을 생각하는 것이 아닌 최댓값의 기준으로 바라보는 것 -> 굉장히 신선
from heapq import heappush, heappop, heapify
def solution(stones, k):
    heap = [(-1*val, idx) for idx, val in enumerate(stones[:k])]
    heapify(heap)
    answer = -1*heap[0][0]

    for i in range(k, len(stones)):
        heappush(heap, (-1*stones[i], i))
        # 현재, 윈도우 상 있으면 안되는데, 최댓값인 애라면 삭제
        while heap[0][1] <= i-k:
            heappop(heap)

        answer = min(answer, -1*heap[0][0])

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
