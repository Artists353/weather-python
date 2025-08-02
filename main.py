import requests

def get_coordinates(city, api_key):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            lat = data['results'][0]['geometry']['lat']
            lon = data['results'][0]['geometry']['lng']
            return lat, lon
        else:
            print("Город не найден.")
            return None, None
    else:
        print("Ошибка при получении координат.")
        return None, None

def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_weather = data.get('current_weather', {})
        if current_weather:
            print(f"Температура: {current_weather['temperature']}°C")
            print(f"Ветер: {current_weather['windspeed']} м/с")
            print(f"Направление ветра: {current_weather['winddirection']}°")
        else:
            print("Данные о текущей погоде недоступны.")
    else:
        print("Ошибка при получении данных о погоде.")

# Ввод названия города
city = input("Введите название города: ")

# Ваш API-ключ для OpenCage
api_key = "0712f554deb84d87b3d5a0fe0c494c27"

# Получение координат
latitude, longitude = get_coordinates(city, api_key)

# Если координаты найдены, получить погоду
if latitude is not None and longitude is not None:
    get_weather(latitude, longitude)
