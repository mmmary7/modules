import requests
import random
from bs4 import BeautifulSoup


def facts():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_ = 'p-2 clearfix'))

    print(fact.text)
    print(fact.a.attrs['href'])


def get_fest():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content

    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='social-group'))

    print(fest.text)


#facts()
get_fest()