import sys


def solution(n, costs):
    parent = [i for i in range(n)]
    answer = 0
    costs.sort(key=lambda x: x[2])

    def find(a):
        if parent[a] == a:
            return a
        else:
            parent[a] = find(parent[a])
            return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return True
        elif a < b:
            parent[b] = a
            return False
        else:
            parent[a] = b
            return False

    for cost in costs:
        if union(cost[0], cost[1]):
            continue
        answer += cost[2]
        end = 0
        for idx, pare in enumerate(parent):
            if idx != pare:
                parent[idx] = find(pare)
                end += 1
        if end == n-1:
            break

    return answer


print(solution(5,  [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))