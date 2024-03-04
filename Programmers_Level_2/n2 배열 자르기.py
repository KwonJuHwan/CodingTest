def solution(n, left, right):
    answer = []
    y_left = left // n + 1
    x_left = left % n
    i = left
    while i <= right:
        # 2
        y = i // n + 1
        x = i % n
        for j in range(n):
            if i > right:
                break
            if x <= j:
                if j < y:
                    answer.append(y)
                else:
                    answer.append(j + 1)
                i += 1

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
