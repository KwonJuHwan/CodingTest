## https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

def solution(board, skill):
    answer = 0
    new_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for sk in skill:
        if sk[0] == 1:
            new_board[sk[1]][sk[2]] -= sk[5]
            new_board[sk[1]][sk[4]+1] += sk[5]
            new_board[sk[3]+1][sk[2]] += sk[5]
            new_board[sk[3]+1][sk[4]+1] -= sk[5]
        if sk[0] == 2:
            new_board[sk[1]][sk[2]] += sk[5]
            new_board[sk[1]][sk[4]+1] -= sk[5]
            new_board[sk[3]+1][sk[2]] -= sk[5]
            new_board[sk[3]+1][sk[4]+1] += sk[5]
    ## 위에서 아래로 누적합
    for i in range(1,len(new_board)):
        for j in range(len(new_board[0])):
            new_board[i][j] += new_board[i-1][j]
    ## 왼쪽에서 오른쪽으로 누적합
    for i in range(len(new_board)):
        for j in range(1, len(new_board[0])):
            new_board[i][j] += new_board[i][j-1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += new_board[i][j]

    for bo in board:
        for b in bo:
            if b > 0:
                answer += 1

    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
