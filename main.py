import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

# Передача параметра в запросе.
payload = {"name": "Dasha"}
response_1 = requests.get("https://playground.learnqa.ru/api/hello",params=payload)
print(response_1.text)

# Ex4: GET-запрос
#
# В проекте создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
# Затем с помощью функции print вывести содержимое текста в ответе на запрос.
# Когда скрипт будет готов - давайте его закоммитим в наш репозиторий.

response_one = requests.get("https://playground.learnqa.ru/api/get_text")
print(response_one.text)

# Парсим полученный ответ








