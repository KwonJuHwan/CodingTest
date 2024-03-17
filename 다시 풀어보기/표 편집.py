# 직접 삭제하는 것은 오류가 많으니, 배열 or 연결리스트를 이용하여 구현
# 베열 사용시, 인덱스 이동에서 O(n)의 시간복잡도를 가지므로, 비효율적 -> 연결리스트 이용
# 연결리스트 자료구조를 사용하는 문제는 처음이므로, 핋히 복습
# 연결리스트만 떠올리면 그 다음부터는 직접 예시를 들어가며 구현
# 처음과 끝의 예외처리를 항상 생각하면서 구현 <= 연결리스트 구현의 핵심

def solution(n, k, cmd):
    now = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n - 2, None]
    answer = ["O"] * n
    stack = []
    for c in cmd:
        if c == "C":
            answer[now] = "X"
            prev, next = table[now]
            stack.append((now, prev, next))
            # 포인터 이동
            if next is None:
                now = table[now][0]
            else:
                now = table[now][1]
            # 처음과 끝 예외 처리
            if prev is None:
                table[next][0] = None
            elif next is None:
                table[prev][1] = None
            # 중간 값 처리
            else:
                table[prev][1] = next
                table[next][0] = prev
        elif c == "Z":
            last_idx, last_pre, last_next = stack.pop()
            answer[last_idx] = "O"
            if last_pre is None:
                table[last_next][0] = last_idx
            elif last_next is None:
                table[last_pre][1] = last_idx
            else:
                table[last_pre][1] = last_idx
                table[last_next][0] = last_idx
        else:
            cmd, x = c.split(" ")
            if cmd is "U":
                for i in range(int(x)):
                    now = table[now][0]
            else:
                for i in range(int(x)):
                    now = table[now][1]

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
