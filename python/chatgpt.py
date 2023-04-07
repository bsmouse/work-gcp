import requests

data = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-type': 'application/json'}

response = requests.post('https://www.google.com/post',
                         json=data, headers=headers)
print(response.status_code)  # 응답 코드 출력
print(response.content)  # 응답 내용 출력
