import requests

target = 'Петровка,38'

response = requests.get(f'http://geocode-maps.yandex.ru/1.x/?geocode={target}&format=json')
if response:
    json_response = response.json()

    print(json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
        'metaDataProperty']['GeocoderMetaData']['Address']['postal_code'])
