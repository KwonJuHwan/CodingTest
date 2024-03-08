from collections import Counter


def solution(gems):
    gem_list = set(gems)
    gem_dict = {gems[0]: 1}
    gem_len = len(gem_list)
    left, right = 0, 0
    ## 전체 길이로 초기화
    answer = [0, len(gems) - 1]
    while left <= right and right < len(gems):
        # 모든 보석을 가지고 있는 경우
        if len(gem_dict) >= gem_len:
            # 현재 갱신중인 최소 길이보다 짧을 때 -> 업데이트
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            # 최소 길이를 찾기 위한, 앞쪽 보석 구매 X
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] <= 0:
                del gem_dict[gems[left]]
            left += 1
        # 보석 구매
        else:
            right += 1
            # 더 이상 추가할 보석이 없을 경우
            if right >= len(gems):
                break
            # 추가할 보석이 이미 가지고 있는 경우
            if gems[right] in gem_dict.keys():
                gem_dict[gems[right]] += 1
            # 없으면 초기화
            else:
                gem_dict[gems[right]] = 1

    return [answer[0] + 1, answer[1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
