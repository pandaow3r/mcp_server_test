import requests
import json

def get_coordinates(city_name: str):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    try:
        response = requests.get(url, headers={"User-Agent": "weather-app"})
        data = response.json()
        if data:
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            return float(latitude), float(longitude)
        else:
            return None, None
    except Exception as e:
        return None, None

def getWeatherInfo(location: str) -> str:
    latitude, longitude = get_coordinates(location)
    if latitude is None or longitude is None:
        return f"{location} için koordinat bulunamadı. Lütfen geçerli bir şehir adı girin."

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    try:
        response = requests.get(url)
        data = response.json()
        times = data["hourly"]["time"]
        temps = data["hourly"]["temperature_2m"]
        if times and temps:
            # En güncel (şu anki) sıcaklığı almak için ilk değeri alıyoruz
            current_temp = temps[0]
            return f"{location} için güncel sıcaklık: {current_temp}°C"
        else:
            return f"{location} için sıcaklık verisi bulunamadı."
    except Exception as e:
        return f"Hava durumu alınırken hata oluştu: {str(e)}"