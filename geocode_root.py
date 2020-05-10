import requests
import json


def show_on_map(destination):
    response = requests.get("http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&"
                            "geocode={}&format=json".format(destination))
    response = response.content
    data = json.loads(response)
    deta = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    coords = deta["Point"]["pos"].split()
    map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&l=map&z=10&pt={},{},pm2gnm&size=600,450". \
        format(coords[0], coords[1], coords[0], coords[1])
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
