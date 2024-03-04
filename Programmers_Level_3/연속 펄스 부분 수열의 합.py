def solution(sequence):
    next1 = [sequence[i] * (-1) ** i for i in range(len(sequence))]
    next2 = [sequence[i] * (-1) ** (i + 1) for i in range(len(sequence))]
    dp1 = [sequence[i] * (-1) ** i for i in range(len(sequence))]
    dp2 = [sequence[i] * (-1) ** (i + 1) for i in range(len(sequence))]

    for i in range(1, len(sequence)):
        # 버리는 것이 이득인가, 계속 더해가는게 이득인가 판단
        dp1[i] = max(dp1[i - 1] + next1[i], next1[i])
        dp2[i] = max(dp2[i - 1] + next2[i], next2[i])
    # dp에는 각 부분별 최대 합들이 들어가있음
    answer = max(max(dp1),max(dp2))
    return answer


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
