# 심사시간을 최대로 잡고, 이분탐색으로 줄여가며 최소시간 찾기
# left, right가 심사관 idx가 아닌, 총 걸리는 시간 -> 시간을 찾는 것이므로

def solution(n, times):
    answer = 0
    times.sort()
    left = 0
    # 최대 시간
    right = n * times[-1]
    while left <= right:
        mid = (right + left) // 2
        person = 0
        # 주어진 시간안에 각 심사관마다 심사할 수 있는 사람 수 합계
        for i in range(len(times)):
            person += mid // times[i]
        # 주어진 시간안에 심사를 못할경우 -> 시간을 늘려야 함
        if person < n:
            left = mid + 1
        # 주어진 시간 안에 심사가 가능 -> 최소 시간을 구해야 함
        else:
            right = mid - 1
    return right+1

print(solution(6,[7, 10]))

