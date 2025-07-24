import requests

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

# Координаты Ростова-на-Дону
coordinates_latitude = int(input("Введите координаты широты: "))
coordinates_longitude = int(input("введите координаты долготы: "))
latitude = coordinates_latitude
longitude = coordinates_longitude

get_weather(latitude, longitude)