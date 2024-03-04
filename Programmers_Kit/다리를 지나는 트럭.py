def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer
[1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 1, 2, 3] // [12, 5, 4, 3, 2, 1, 6, 5, 2, 1, 2, 1, 0]
[1, 2, 3, 4, 1] // [4, 3, 2, 1, 0]
[5, 4, 3, 2, 5] // [1, 1, 1, 1, 0]
[1, 2, 3, 2, 3, 1] // [5, 4, 1, 2, 1, 0]