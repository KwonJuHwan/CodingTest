import json

# 숫자 리스트 생성
numbers_list = [1, 2, 3, 4, 5]

# 리스트를 JSON 형식으로 변환
json_data = json.dumps(numbers_list)

# 결과 출력
print(json_data)