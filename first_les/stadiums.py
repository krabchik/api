import pygame
import requests
import sys

targets = ['Спартак', 'Динамо', 'Лужники']
coords = []

for target in targets:
    response = requests.get(f'http://geocode-maps.yandex.ru/1.x/?geocode={target}&format=json')
    if response:
        json_response = response.json()
        i = 0 if target != 'Спартак' else 4
        pos = json_response['response']['GeoObjectCollection']['featureMember'][i]['GeoObject']['Point'][
            'pos']
        coords.append(','.join(pos.split()))
print(coords)
try:
    map_request = f"http://static-maps.yandex.ru/1.x/?l=sat&pt={',pm2gnm~'.join(coords)},pm2gnm"
    response = requests.get(map_request)
    print(map_request)
except:
    print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()