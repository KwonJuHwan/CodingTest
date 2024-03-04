from itertools import combinations


def solution(orders, course):
    answer = []
    s_set = set()
    for n in course:
        for order in orders:
            # 가능한 조합 넣기 // sorted를 이용해서 WX == WX 중복 제거
            if len(order) >= n:
                for cour in combinations(order, n):
                    s_set.add(tuple(sorted(cour)))
        max_score = 2
        max_result = []
        while len(s_set) > 0:
            pop_list = s_set.pop()
            pop_score = 0
            for order in orders:
                no_in = False
                # 문자 열로 보는 것이 아닌 하나 하나의 char 로 봐야함
                for pop in pop_list:
                    if pop not in order:
                        no_in = True
                if not no_in:
                    pop_score += 1
            if max_score <= pop_score:
                max_score = pop_score
                max_result.append((max_score, pop_list))
        max_result.sort(key=lambda x: x[1])
        for result in max_result:
            if result[0] == max_score:
                answer.append(result[1])
    answer.sort()
    answer_list = []
    for q in answer:
        e = ""
        for w in q:
            e += w
        answer_list.append(e)
    return answer_list


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
print(solution(["ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE"], [2, 3, 5]))
