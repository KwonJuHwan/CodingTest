# 직접 삭제하는 것은 오류가 많으니, 배열 or 연결리스트를 이용하여 구현
# 베열 사용시, 인덱스 이동에서 O(n)의 시간복잡도를 가지므로, 비효율적 -> 연결리스트 이용
# 연결리스트 자료구조를 사용하는 문제는 처음이므로, 핋히 복습

def solution(n, k, cmd):
    cur = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
