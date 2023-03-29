import requests

def heroes_request():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    return response.json()

def find_most_int(json_link, list_of_heroes):
    dict_of_heroes = {}
    for item in json_link:
        if item['name'] in list_of_heroes:
            dict_of_heroes[item['name']] = item['powerstats']['intelligence']
    dict_of_heroes = dict(sorted(dict_of_heroes.items(), key=lambda item: item[1], reverse=True))

    return list(dict_of_heroes.keys())[0], list(dict_of_heroes.values())[0]