def parse_weather_data(weather_data):
    if weather_data is None:
        return None, None
    
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    feels_like = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    visibility = weather_data['visibility']
    wind_speed = weather_data['wind']['speed']
    latitude = weather_data['coord']['lat']
    longitude = weather_data['coord']['lon']
    
    return temperature, humidity, feels_like, temp_min, temp_max, pressure, visibility, wind_speed, latitude, longitude