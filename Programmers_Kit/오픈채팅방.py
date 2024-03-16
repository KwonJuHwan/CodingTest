def solution(record):
    answer = []
    name_dict = {}

    for now in record:
        cmd = now.split(" ")
        if cmd[0] == "Enter":
            answer.append(cmd[1] + " 들어왔습니다.")
            name_dict[cmd[1]] = cmd[2]
        elif cmd[0] == "Leave":
            answer.append(cmd[1] + " 나갔습니다.")
        else:
            name_dict[cmd[1]] = cmd[2]
    for i, ans in enumerate(answer):
        uid, cmd = ans.split(" ")
        answer[i] = name_dict[uid] + "님이 " + cmd

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
