from collections import deque

def solution(maps):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    x_len=len(maps)
    y_len=len(maps[0])
    answer_list=[]
    q=deque()

    q.append((0,0))
    while q:
        x,y = q.popleft()
        if x==x_len-1 and y== y_len-1:
            answer_list.append(maps[x][y])
        for i in range(4):
            sx=x+dx[i]
            sy=y+dy[i]
            if 0<=sx<x_len and 0<=sy<y_len :
                if maps[sx][sy]==1:
                    maps[sx][sy]=maps[x][y]+1
                    q.append((sx,sy))
    if len(answer_list)==0:
        answer= -1
    else:
        answer = min(answer_list)
    print(maps)
    return answer