# 투 포인터의 예시로 좋은 문제

def solution(gems):
    gem_list = set(gems)
    len_gems = len(gem_list)
    left, right = 0, 0
    gem_dict = {gems[0]: 1}
    answer = [0, len(gems)-1]
    while left < len(gems) and right < len(gems):
        # 모든 보석을 포함 한다면
        if len(gem_dict) == len_gems:
            # 최소 길이 라면
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            # 아니면 left 올려서 최소 길이 탐색
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]
                left += 1
        else:
            right += 1
            # index over 방지
            if right == len(gems):
                break
            # dictionary에 있으면 개수 늘리기
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            # 없으면 최초 초기화
            else:
                gem_dict[gems[right]] = 1
    return [answer[0] + 1, answer[1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
