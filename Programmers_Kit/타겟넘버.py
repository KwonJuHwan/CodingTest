from collections import deque

def solution(numbers, target):
    answer = 0
    q=deque()
    q.append((0,numbers[0]))
    q.append((0,-numbers[0]))
    while q:
        now_index, now = q.pop()
        if now_index == len(numbers)-1:
            if now==target :
                answer+=1
            continue
        q.append((now_index+1, now+numbers[now_index+1]))
        q.append((now_index+1, now-numbers[now_index+1]))

    return answer