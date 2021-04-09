import requests
from datetime import datetime

user_api = "c1d2ef4f11414f7c642cda7dcf3da271"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
if api_data['cod']=='404':
    print("Invalid city name")

else:
    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    temperature = str(temp_city)
    weather = str(weather_desc)
    wind_speed = str(wind_spd)
    date_time_city = str(date_time)


    WeatherFile = open("C:/Users/USER/PycharmProjects/weather/niveda.txt", 'a+')
    WeatherFile.write("---------------------------------------------------\n")
    WeatherFile.write("City name-->")
    WeatherFile.write( location  +'\n')
    WeatherFile.write("Temperature-->")
    WeatherFile.write( temperature +'\n')
    WeatherFile.write("Weather Description-->")
    WeatherFile.write(weather + '\n')
    WeatherFile.write("Wind speed-->")
    WeatherFile.write(wind_speed + '\n')
    WeatherFile.write("Date and time of the city-->")
    WeatherFile.write(date_time_city + '\n')
    WeatherFile.write("---------------------------------------------------\n")

    WeatherFile.read()
    WeatherFile.close()

