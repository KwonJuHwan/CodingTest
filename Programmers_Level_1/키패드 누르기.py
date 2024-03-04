def solution(numbers, hand):
    keyPad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]
    left = keyPad[3][0]
    right = keyPad[3][2]
    answer = ''
    for num in numbers:
        left_score = 0
        right_score = 0
        x, y = 0, 0
        # 위치 지정
        for i in range(len(keyPad)):
            for j in range(len((keyPad[0]))):
                if keyPad[i][j] == num:
                    x = i
                    y = j
                    break
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = keyPad[x][y]
            continue
        if num == 3 or num == 6 or num == 9:
            answer += "R"
            right = keyPad[x][y]
            continue
        # left , right  위치 찾기
        for i in range(len(keyPad)):
            for j in range(len((keyPad[0]))):
                if left == keyPad[i][j]:
                    left_score = abs(i - x) + abs(j - y)
                if right == keyPad[i][j]:
                    right_score = abs(i - x) + abs(j - y)
            # 점수 부여
        if left_score == right_score:
            if hand == "right":
                right = keyPad[x][y]
                answer += "R"
            else:
                left = keyPad[x][y]
                answer += "L"
        if left_score > right_score:
            right = keyPad[x][y]
            answer += "R"
        if left_score < right_score:
            left = keyPad[x][y]
            answer += "L"
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
