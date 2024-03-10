# dp 의 입장에선 현재 스티커를 뗄 수 있냐, 없냐 / 이전의 스티커를 뗐는지 안 뗐는지만 알면 됨 /  

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2 = [0] * len(sticker)
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(max(dp1), max(dp2))


