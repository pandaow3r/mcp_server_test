import requests
import json

def getWeatherInfo(location: str) -> str:
    # Şehir adına göre koordinatları belirle (örnek: Berlin)
    # Gerçek uygulamada bir şehir->koordinat eşlemesi yapılabilir
    if location.lower() == "berlin":
        latitude = 52.52
        longitude = 13.41
    else:
        return f"{location} için hava durumu bilgisi bulunamadı. Sadece 'Berlin' destekleniyor."

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    try:
        response = requests.get(url)
        data = response.json()
        # Son saatin sıcaklığını al
        times = data["hourly"]["time"]
        temps = data["hourly"]["temperature_2m"]
        if times and temps:
            current_temp = temps[0]
            return f"{location} için güncel sıcaklık: {current_temp}°C"
        else:
            return f"{location} için sıcaklık verisi bulunamadı."
    except Exception as e:
        return f"Hava durumu alınırken hata oluştu: {str(e)}"