import requests

def get_ip_and_location():
    try:
        ip_info = requests.get('https://ipinfo.io/json')
        ip_data = ip_info.json()
        ip_address = ip_data['ip']
        print("Ваш IP-адрес:", ip_address)

        location = ip_data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        print("Ваше местоположение (широта, долгота):", latitude, longitude)

        city = ip_data['city']
        region = ip_data['region']
        country = ip_data['country']
        print("Ваш город:", city)
        print("Ваш регион:", region)
        print("Ваша страна:", country)

    except Exception as e:
        print("Ошибка при получении информации о местоположении:", e)

if __name__ == "__main__":
    get_ip_and_location()
