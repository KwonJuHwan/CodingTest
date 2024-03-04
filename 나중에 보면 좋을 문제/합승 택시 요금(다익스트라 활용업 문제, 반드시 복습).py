
import heapq


def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for f in fares:
        node1, node2, fee = f
        # node1 - > node2 가는 요금이 fee
        graph[node1].append((node2, fee))
        # node2 - > node1 가는 요금이 fee
        graph[node2].append((node1, fee))

    def dijkstra(s):
        q = []
        # 최단거리 테이블을 무한으로 초기화
        distance = [INF] * (n + 1)
        # 거리(금액), 노드번호 순서
        heapq.heappush(q, (0, s))
        # 시작노드로 가는 최단거리는 0
        distance[s] = 0

        while q:
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 노드면 무시
            if distance[now] < dist:
                continue

            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        return distance

    distance_list = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    k_list = [[]]
    print(distance_list)

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
