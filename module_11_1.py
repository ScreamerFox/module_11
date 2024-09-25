import datetime
import requests
from pprint import pprint
from weatherapi.models.astronomy import Astronomy
import translators as ts


st = datetime.datetime.now()
today = datetime.datetime.now()

# Форматируем дату
formatted_date = today.strftime("%d.%m.%Y")

API_KEY = '18da05fe144644a1969140903242409'


def choice_city():
    city = int(input(f'Выбирете город из списка:\n1-Москва,\n2-Челябинск,\n3-Ленинград,\n4-Санкт-Петербург,\n5-Новосибирск,\n6-Екатеринбург\nВаш выбор: '))
    if city == 1:
        return 'Moscow'
    elif city == 2:
        return 'Chelyabinsk'
    elif city == 3:
        return 'Leningrad'
    elif city == 4:
        return 'Peterburg'
    elif city == 5:
        return 'Novosibirsk'
    elif city == 6:
        return 'Ekaterinburg'


def tt(text): # Переводим текст с английского на русский
    return (ts.translate_text(text, translator='yandex', to_language='ru'))


def general_data(city): # Получаем основные данные о погоде
    SITE_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes&lang=ru'
    response = requests.get(SITE_URL)
    if response.status_code == 200:
        # Парсим ответ в формате JSON
        data = response.json()

        # Получаем текущие данные
        ct = data['location']['country']
        datetime_n = data['location']['localtime']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        temp_f = data['current']['temp_f']
        wind_kph = data['current']['wind_kph']

        print(f'Текущая погода в городе {tt(city)}, {tt(ct)}, на {datetime_n}:')
        print(f'Температура в градусах: {temp_c}°C, {temp_f}°F')
        print(f'Скорость ветра: {wind_kph} км/ч')
        print(f'Состояние: {condition}')

def astronomy_data(city): # Получаем астрономические данные о лунной фазе и восходе солнца
    astro_url = f'https://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q={city}&dt={formatted_date}'
    response = requests.get(astro_url)

    if response.status_code == 200:
        # Парсим ответ в формате JSON
        data = response.json()
        # Получаем астрономические данные:
        moon_phase = data['astronomy']['astro']['moon_phase']
        sunrise = data['astronomy']['astro']['sunrise']

        # Выводим полученные данные:
        print(f'Фаза луны: {tt(moon_phase)}')
        print(f'Восход солнца: {sunrise}')

def air_data(city): # Получаем данные воздуха
    SITE_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes&lang=ru'
    response = requests.get(SITE_URL)

    if response.status_code == 200:
        # Парсим ответ в формате JSON
        data = response.json()
        # Получаем данные воздуха:
        co = data['current']['air_quality']['co']
        no2 = data['current']['air_quality']['no2']
        o3 = data['current']['air_quality']['o3']

        print(f'Концентрация CO: {co}ppm')
        print(f'Концентрация NO2: {no2}ppm')
        print(f'Концентрация O3: {o3}ppm')


main_menu = input(f'Хотите узнать данные о погоде или воспользоваться переводчиком? (погода\перевод): ')
if main_menu.lower() == 'погода':
    a = choice_city()
    general_data(a)
    astronomy_data(a)
    air_data(a)
elif main_menu.lower() == 'перевод':
    text = input('Введите текст для перевода: ')
    print(tt(text))


end = datetime.datetime.now()
print(end - st)
