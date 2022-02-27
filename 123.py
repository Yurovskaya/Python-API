# Cookie
import requests

payload = {"login":"secret_login","password":"secret_pass"}
response_12 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response_12.text)
print(response_12.status_code)
print(dict(response_12.cookies))
