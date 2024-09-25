import datetime
import requests
from pprint import pprint
from weatherapi.models.astronomy import Astronomy
import translators as ts


API_KEY = '18da05fe144644a1969140903242409'
city = 'Chelyabinsk'
SITE_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes&lang=ru'
astro_url = f'https://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q=Chelyabinsk&dt=25.09.2024'

def tt(text): # Переводим текст с английского на русский
    return (ts.translate_text(text, translator='yandex', to_language='ru'))


def general_data(): # Получаем основные данные о погоде
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

def astronomy_data(): # Получаем астрономические данные о лунной фазе и восходе солнца
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

def air_data(): # Получаем данные воздуха
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


general_data()
astronomy_data()
air_data()

