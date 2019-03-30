import requests

cities = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

for city in cities:
    response = requests.get(f'http://geocode-maps.yandex.ru/1.x/?geocode={city}&format=json')
    if response:
        json_response = response.json()

        print(city, '-', end=' ')
        print(json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
            'metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]['name'])
