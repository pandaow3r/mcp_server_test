import requests
import json
from datetime import datetime, timezone

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
            # Şu anki UTC saatine en yakın zamanı bul
            now_utc = datetime.now(timezone.utc)
            time_diffs = [abs((datetime.fromisoformat(t).replace(tzinfo=timezone.utc) - now_utc).total_seconds()) for t in times]
            closest_idx = time_diffs.index(min(time_diffs))
            current_temp = temps[closest_idx]
            current_time = times[closest_idx].replace('T', ' ')
            return f"{location} için {current_time} saatindeki sıcaklık: {current_temp}°C"
        else:
            return f"{location} için sıcaklık verisi bulunamadı."
    except Exception as e:
        return f"Hava durumu alınırken hata oluştu: {str(e)}"