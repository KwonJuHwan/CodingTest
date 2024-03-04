import sys

sys.setrecursionlimit(10 ** 6)


# dfs 중,누적 되는 변수가 있으면 안됨
def solution(users, emoticons):
    d_list = [0.9, 0.8, 0.7, 0.6]
    answer = []
    for user in users:
        user[0] = (100 - user[0]) * 0.01
    answer_list = []
    dis_list = [0] * len(emoticons)

    def dfs(now):
        if now == len(emoticons):
            n = 0
            m = 0
            sum_list = [0 for _ in range(len(users))]
            for x in range(len(users)):
                for y in range(len(emoticons)):
                    if dis_list[y] <= users[x][0]:
                        sum_list[x] += dis_list[y] * emoticons[y]
            for x in range(len(users)):
                if sum_list[x] >= users[x][1]:
                    n += 1
                else:
                    m += sum_list[x]
            answer_list.append((n, m))
            return 0
        for i in range(4):
            dis_list[now] = d_list[i]
            dfs(now + 1)

    dfs(0)
    answer_list.sort(key=lambda x: (-x[0], -x[1]))
    answer.append(answer_list[0][0])
    answer.append(int(answer_list[0][1]))
    return answer


    dfs(0, [0 for _ in range(len(users))])

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
