from bs4 import BeautifulSoup
import urllib.request
import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
response = urllib.request.urlopen('http://rapidmetrogurgaon.com/calculator.aspx')
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

stations = []
station_map = {}

for name in soup.find_all('option'):

    station_name = name.get_text()

    if station_name not in station_map or station_map[station_name] < 1:
        params = {'address': station_name + ' metro station, delhi, India'}
        print("params : ", params)
        r = requests.get(url=url, params=params)

        # extracting data in json format
        data = r.json()

        coords = data['results'][0]['geometry']['location']
        pincode = 110001

        print(data)
        for address in data['results'][0]['address_components']:
            if 'postal_code' in address['types']:
                pincode = address['long_name']

        station = {
            "name": station_name,
            "state": "New Delhi",
            "pincode": pincode,
            "coords": coords,
            "address": data['results'][0]['formatted_address']
        }

        stations.append(station)

        station_map[station_name] = 1

print(stations)
