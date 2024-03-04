import string, math

temp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]


def is_primitive(num):
    primitive = True
    if num == 1:
        primitive = False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                primitive = False
    return primitive


def solution(n, k):
    num = convert(n, k)
    s = ""
    pri_list = []
    answer = 0
    for i in range(len(num)):
        if num[i] != "0":
            s += num[i]
            if i == len(num) - 1:
                pri_list.append(s)
        elif s != "":
            pri_list.append(s)
            s = ""
    for pri in pri_list:
        if is_primitive(int(pri)):
            answer += 1
    return answer

