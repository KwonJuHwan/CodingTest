def solution(cacheSize, cities):
    answer = 0
    cache = []
    # cache init
    for i in range(cacheSize):
        cache.append(("", -i))

    for idx, city in enumerate(cities):
        Acity = ""
        # 대문자로 통일
        for c in city:
            if ord(c) >= 97:
                c = chr(ord(c)- 32)
            Acity += c
        caching_true = False
        # 캐시 확인
        for cachIdx, caching in enumerate(cache):
            # cache hit
            if caching[0] == Acity:
                del cache[cachIdx]
                cache.append((Acity, idx))
                answer += 1
                caching_true = True
                break
        # cache miss
        if not caching_true:
            min_change = [cache[0][1], 0]
            for cachIdx, caching in enumerate(cache):
                if min_change[0] > caching[1]:
                    min_change = [caching[1], cachIdx]
            del cache[min_change[1]]
            cache.append((Acity, idx))
            answer += 5
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))