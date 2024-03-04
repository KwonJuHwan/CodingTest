def solution(fees, records):
    answer = []
    in_list = {}
    answer_list = []
    for record in records:
        car_num = record[6:10]
        now_time = int(record[0:2]) * 60 + int(record[3:5])
        # 출차
        if car_num in in_list:
            time = now_time - in_list[car_num]
            del in_list[car_num]
            answer_list.append((car_num, time))
        # 입차
        else:
            in_list[car_num] = now_time

    # 출차 기록이 없는 차 처리
    for car_num, now_time in in_list.items():
        time = (23 * 60 + 59) - now_time
        answer_list.append((car_num, time))
    answer_list.sort(key=lambda x: x[0])
    print(answer_list)
    # 종합 계산
    calculated = []
    for ans_1 in answer_list:
        now_car = ans_1[0]
        if now_car not in calculated:
            time = 0
            calculated.append(now_car)
            for ans_2 in answer_list:
                if ans_2[0] == now_car:
                    time += ans_2[1]
            # 기본 요금
            if time <= fees[0]:
                answer.append(fees[1])
            # 기본 요금 이상
            else:
                if (time - fees[0]) % fees[2] == 0:
                    fee = fees[1] + ((time - fees[0]) // fees[2]) * fees[3]
                else:
                    fee = fees[1] + (((time - fees[0]) // fees[2]) + 1) * fees[3]
                answer.append(fee)
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
