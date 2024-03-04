def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations)):
        now = citations[i]
        if (i + 1) >= now:
            answer = now
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
