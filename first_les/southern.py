import requests
import sys

cities = sys.argv[1:]

max_coords = 0
southern_city = ''
response = None

for i in cities:
    try:
        response = requests.get(f'http://geocode-maps.yandex.ru/1.x/?geocode={i}&format=json')
    except Exception as e:
        print('Не удается подключиться к сети Интернет, попробуйте еще раз')
        sys.exit()

    if response:
        json_response = response.json()
        try:
            south = \
                json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
                    'Point'][
                    'pos'][1]
        except IndexError:
            print(i, 'IndexError')
        if south == '.':
            print(i, '.')
            continue
        south = float(south)
        if float(south) > max_coords:
            southern_city = i
            max_coords = south
    else:
        print('Что-то пошло не так, попробуйте позже')
print(southern_city)
