def solution(n, wires):
    answer = -1
    parent = [0] * (n + 1)

    def find(a):
        if parent[a] == a:
            return a
        else:
            parent[a] = find(parent[a])
            return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    li = []
    for i in range(len(wires)):
        for j in range(1, n + 1):
            parent[j] = j

        for j in range(len(wires)):
            if i == j:
                continue
            x, y = wires[j][0], wires[j][1]
            union(x, y)
        for j in range(1, n + 1):
            parent[j]=find(j)

        count = [0] * (n + 1)
        answer_list = []
        for j in range(1, n + 1):
            count[parent[j]] += 1
        for j in range(1, n + 1):
            if count[j] != 0:
                answer_list.append(count[j])
        if answer_list[0] <= answer_list[1]:
            li.append(answer_list[1] - answer_list[0])
        else:
            li.append(answer_list[0] - answer_list[1])
    answer = min(li)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
