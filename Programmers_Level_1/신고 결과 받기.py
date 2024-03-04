def solution(id_list, report, k):
    answer = []
    id_dic = {}
    report_dic = {}
    report_set = set()
    for id in id_list:
        id_dic[id] = []
        report_dic[id] = 0
    # 신고
    for rep in report:
        report_set.add(rep)
    for rep in report_set:
        rep_split = rep.split(" ")
        report_dic[rep_split[1]] += 1
        id_dic[rep_split[0]].append(rep_split[1])
    # 신고 K번 이상된 사람들 저장
    report_list = []
    for key in report_dic.keys():
        if report_dic[key] >= k:
            report_list.append(key)

    # id 마다 신고 개수 세기
    for id in id_list:
        cnt = 0
        for repo in report_list:
            if repo in id_dic[id]:
                cnt += 1
        answer.append(cnt)
    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"]	,3))