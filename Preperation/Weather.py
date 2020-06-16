import socket
import requests
try:
    socket.create_connection(("www.google.com",80))
    res = requests.get("https://ipinfo.io/")
    data = res.json()
    city = data['city']
    a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2="&q="+city
    a3="&appid=c6e315d09197cec231495138183954bd"
    api_address=a1+a2+a3
    res1=requests.get(api_address)
    data=res1.json()
    temp1=data['main']['temp']
    print(city)
    print("temo1 = ",temp1)
except OSError as e:
    print("Check Network",e)
