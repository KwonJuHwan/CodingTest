from collections import deque


def solution1(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


print(solution1("{{2},{2,1},{1,2,1},{1,1,1,2}}"))
print(solution1("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution1("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution1("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution1("{{20,111},{111}}"))
print(solution1("{{123}}"))
