# 다양한 자료구조를 활용하여, 주어진 조건에 맞게 문제 해결
import copy

def solution(skill, skill_trees):
    answer = 0
    skill = skill[::-1]
    skill_stack = list(skill)
    skill_dict = {}
    # 현재 가능한 스킬 여부를 판단하는 skill_dict 선언
    for s in skill_stack:
        skill_dict[s] = False
    skill_dict[skill_stack.pop()] = True

    for now_skill in skill_trees:
        now_dict = copy.deepcopy(skill_dict)
        now_stack = copy.deepcopy(skill_stack)
        x = False
        for now in now_skill:
            # 선행 스킬이 존재하는 스킬
            if now in now_dict.keys():
                if not now_dict[now]:
                    x = True
                    break
                if now_dict[now] and now_stack:
                    now_dict[now_stack.pop()] = True

        if not x:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
