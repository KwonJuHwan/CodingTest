def solution(s):
    answer = 1
    # 홀수 팰린 체크
    if len(s) % 2 == 1:
        mid = len(s) // 2
    else:
        mid = (len(s) // 2) - 1
    for i in range(1, len(s) - 1):
        now = s[i]
        palinSum = 1
        if i <= mid:
            for j in range(1, i + 1):
                if s[i - j] == s[i + j]:
                    palinSum += 2
                else:
                    break
        else:
            for j in range(1, len(s) - i):
                if s[i - j] == s[i + j]:
                    palinSum += 2
                else:
                    break
        answer = max(palinSum, answer)
    # 짝수 팰린 체크
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            now = s[i:j+1]
            if len(now) % 2 == 0:
                k = len(now) // 2
                Palin = True
                for z in range(k):
                    if s[i + z] != s[j - z]:
                        Palin = False
                        break
                if Palin:

                    answer = max(answer, len(now))

    return answer


