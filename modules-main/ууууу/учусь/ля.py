# import emoji
# a = random.randint(1, 10)
import requests
import random
from bs4 import BeautifulSoup
#
# per = requests.get('https://wikiphile.ru/570-fraz-o-motivacii/')
# per = per.content
# soup = BeautifulSoup(per, 'lxml')
# phr = random.choice(soup.find_all('li'))
# print(phr.text)
# url = 'https://fishki.net/2022785-25-chudes-rossii-kotorye-sotvorila-priroda.html'
# response = requests.get(url)
# response = response.content
# print(response)
from requests import get

num = int(input())
source = get(f"https://aws.random.cat/view/{num}").text
if "id=\"cat" in source:
    print(source.split("src=\"")[1].split("\"")[0])
else:
    print("Incorrect id")