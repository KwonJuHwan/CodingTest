# 어떻게 하면 살아남는 숫자가 될 지에 대한, 고민이 부족했음
# 시간 복잡도가 초과될 것 같은 문제의 경우는 그대로 따라가서 브루트 포스를 하는 것이 아닌
# 문제를 분석하고 로직을 구현해야 함.


# 양 쪽의 min 값을 분석해야함 -> min()을 사용하면 시간 초과
# 한쪽 방향으로 밀면서, min 값 최신화
# 하나의 for 문에서 두 개의 로직을 통해, 양쪽의 min 값을 분석하게 하였음
# 투포인터의 장점

import sys

def solution(a):
    result = [False for _ in range(len(a))]
    left_min = sys.maxsize
    right_min = sys.maxsize
    for i in range(len(a)):
        if a[i] < right_min:
            right_min = a[i]
            result[i] = True
        if a[-1-i] < left_min:
            left_min = a[-1-i]
            result[-1-i] = True
    return sum(result)



print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
