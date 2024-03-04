from collections import Counter


def solution(s):
    answer = 0
    word_list = [[] for _ in range(len(s) // 2 + 1)]
    for n in range(len(s) // 2, 0, -1):
        i = 0
        while i + n <= len(s):
            word_list[n].append(s[i:i + n])
            i += 1
    print(word_list)
    for i in range(1,len(s)//2+1):
        count_word = Counter(word_list[i])
    return answer


solution("aabbaccc")
