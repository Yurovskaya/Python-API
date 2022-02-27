# Cookie
import requests
payload = {"login":"secret_login","password":"secret_pass"}
response_12 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",data=payload)

print(response_12.text)
print(response_12.status_code)
print(dict(response_12.cookies))

# Получить куки из запроса
payload = {"login":"secret_login","password":"secret_pass"}
response_13 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",data=payload)

cookie_value = response_13.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
       cookies.update({'auth_cookie': cookie_value})
# Передеать куки в запросе
response_14 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response_14.text)

