import sys, heapq
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    dist = [sys.maxsize for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist[destination] = 0
    q = []
    queue = deque()
    heapq.heappush(q, destination)
    queue.append(destination)
    for i in range(len(roads)):
        graph[roads[i][0]].append(roads[i][1])
        graph[roads[i][1]].append(roads[i][0])

    while queue:
        # pop = heapq.heappop(q)
        pop = queue.popleft()
        if visited[pop]:
            continue
        visited[pop] = True
        for next in graph[pop]:
            if dist[next] > dist[pop] + 1:
                dist[next] = dist[pop] + 1
                queue.append(next)
                # heapq.heappush(q, next)
    for i,d in enumerate(dist):
        if not visited[i]:
            dist[i] = -1
    for source in sources:
        answer.append(dist[source])
    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
