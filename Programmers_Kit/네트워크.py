def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]

    def find(a):
        if parent[a] == a:
            return a
        else:
            parent[a] = find(parent[a])
            return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)
    for i in range(n):
        find(i)

    for i in range(n):
        if parent[i] == i:
            answer += 1
    return answer