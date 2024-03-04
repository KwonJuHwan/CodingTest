# 시간 복잡도 이슈가 있었음
# 부모를 찾으면서 값을 세팅하면 되는 문제였기 때문에 로직은 쉬웠지만, 이름을 숫자로 변경했어야 했기 때문에
# 이름 -> 숫자를 찾는 로직을 그냥 list.index()를 이용하여 찾았었는데, 이는 O(n)의 시간복잡도를 가져
# 시간 초과가 났었다. list.index()를 대신하기 위해 dict()를 사용하여, 찾을때 O(1)의 시간복잡도를 갖게하여, 통과 함

import math

def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    parent = [-1 for _ in range(len(enroll))]
    name = dict()
    for i in range(len(enroll)):
        name[enroll[i]] = i
    # 부모 세팅
    for i in range(len(enroll)):
        if referral[i] == "-":
            parent[i] = -1
            continue
        parent[i] = name[referral[i]]

    # seller 세팅
    for i in range(len(seller)):
        seller[i] = name[seller[i]]
        amount[i] = amount[i]*100

    for i in range(len(seller)):
        now_idx = seller[i]
        now_amount = amount[i]
        while now_idx != -1:
            if now_amount < 1:
                break
            answer[now_idx] += now_amount - math.floor(0.1 * now_amount)
            now_amount = math.floor(0.1 * now_amount)
            now_idx = parent[now_idx]
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
