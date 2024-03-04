from itertools import permutations


def solution(expression):
    answer = 0
    temp = ""
    ori_word_list = []
    ori_operator_list = []

    # 계산식과 숫자 분리
    oper_set = set()
    for i in range(len(expression)):
        if i == len(expression) - 1:
            ori_word_list.append(int(temp + expression[i]))
        if expression[i] == "-" or expression[i] == "*" or expression[i] == "+":
            oper_set.add(expression[i])
            ori_word_list.append(int(temp))
            ori_operator_list.append(expression[i])
            temp = ""
        else:
            temp += expression[i]

    operator_list = []
    word_list = []
    # 수식 경우의 수
    for operators in permutations(oper_set, len(oper_set)):
        for i in ori_operator_list:
            operator_list.append(i)
        if len(word_list) == 1:
            del word_list[0]
        for i in ori_word_list:
            word_list.append(i)
        # print("수식 경우의 수: ", operators)
        for i in range(len(operators)):
            operator = operators[i]
            del_index = []
            # print("oper: ", operator)
            for j in range(len(operator_list)):
                if operator == operator_list[j]:
                    if operator == "-":
                        word_list[j + 1] = word_list[j] - word_list[j + 1]
                    if operator == "+":
                        word_list[j + 1] = word_list[j] + word_list[j + 1]
                    if operator == "*":
                        word_list[j + 1] = word_list[j] * word_list[j + 1]
                    del_index.append(j)
            # print("삭제 전: word_list: ", word_list, " 삭제 할 idx: ", del_index)
            del_index.sort(reverse=True)
            for idx in del_index:
                del word_list[idx]
                del operator_list[idx]
            # print("삭제 후: word_list: ", word_list, " , oper: ", operator_list)
        if word_list[0] < 0:
            word_list[0] = word_list[0] * (-1)
        # print("계산결과: ", word_list[0])
        answer = max(answer, word_list[0])

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
