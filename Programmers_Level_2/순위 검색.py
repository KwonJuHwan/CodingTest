def solution(infos, queries):
    answer = []

    # 총 경우의 수 (108가지)
    info_dict = {}

    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_dict[lang + job + career + food] = []

    # 지원자의 경우의 수 (1인, 16가지)
    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        info_dict[lang + job + career + food].append(int(info[4]))

    # 시간초과를 해결한 방법
    for key in info_dict.keys():
        info_dict[key].sort()

    # 조건
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()

        query_score = int(query[1])
        query = query[0]

        # 점수
        info_score = info_dict[query]
        l = len(info_score)
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if query_score <= info_score[mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(l - tmp)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260",
                "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                "- and - and - and chicken 100", "- and - and - and - 150"]))
