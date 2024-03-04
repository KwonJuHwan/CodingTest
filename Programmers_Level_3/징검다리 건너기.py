def solution(stones, k):
    answer = -1
    stop = True
    while stop:
        length = 0
        answer += 1
        for idx, stone in enumerate(stones):
            if length == k:
                stop = False
                break
            if stone == 0:
                length += 1
            else:
                stones[idx] = stone-1
                length = 0
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
