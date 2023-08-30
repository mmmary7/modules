import requests

url = 'https://swapi.dev/api'
response = requests.get(url).json()

people_api = response.get('people')
planets_api = response.get('planets')
starships_api = response.get('starships')


def check_people(url1):
    for i in range(1, 6):
        response1 = requests.get(f'{url1}/{i}').json()
        print(response1)


def check_planets(url2):
    diametrs_list = []
    for i in range(1, 6):
        response2 = requests.get(f'{url2}/{i}').json()
        print(response2.get('name'))
        diametrs_list.append({response2.get('name') : response2.get('diameter')})
    print(diametrs_list)


def check_starships(url2):
    length_list = []
    for i in range(9, 12):
        response2 = requests.get(f'{url2}/{i}').json()
        length_list.append({response2.get('name'): response2.get('length')})
    print(length_list)


check_starships(starships_api)



