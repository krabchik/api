import requests

response = requests.get(
    "http://geocode-maps.yandex.ru/1.x/?geocode=Красная+площадь,1&format=json")
if response:
    json_response = response.json()

    print(json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['formatted'])
    print(*json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[::-1])