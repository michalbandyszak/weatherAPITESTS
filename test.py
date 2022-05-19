import requests
import unittest
from data import *

api_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
appid = "c54e95f84d456b0dece44b9da8e0c9c6"
lon = (city["coord"]["lon"])
lat = (city["coord"]["lat"])
invalid_lat = 131837.123
invalid_lon = 7771723.123


class GeolocationTests(unittest.TestCase):
    """valid latitude & longitude"""
    def test1(self):
        params = {"lat": lat, "lon": lon, "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 200)
        self.assertEqual(city["name"], find_city.json()["name"])
    """invalid latitude"""
    def test2(self):
        params = {"lat": invalid_lat, "lon": lon, "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 400)

    """invalid longitude"""
    def test3(self):
        params = {"lat": lat, "lon": invalid_lon, "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 400)

    """invalid longitude & invalid latitude"""
    def test4(self):
        params = {"lat": invalid_lat, "lon": invalid_lon, "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 400)
    """empty string as latitude"""
    def test5(self):
        params = {"lat": "", "lon": invalid_lon, "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 400)

    """empty string as longitude"""
    def test6(self):
        params = {"lat": lat, "lon": "", "appid": appid}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 400)

    """empty string as longitude"""

    def test20(self):
        params = {"lat": 52.374, "lon": 4.8897, "appid": appid, "lang": "pl"}
        find_city = requests.get(api_endpoint, params=params)
        self.assertEqual(find_city.status_code, 200)
        self.assertEqual(find_city.json()["name"], "Amsterdam")

    def test21(self):
        params = {"lat": 47.498, "lon": 19.0399,  "appid": appid}
        params_lang = {"lat": 47.498, "lon": 19.0399, "appid": appid, "lang": "kokoloko"}
        find_city = requests.get(api_endpoint, params=params)
        find_city_with_lang = requests.get(api_endpoint, params=params_lang)
        self.assertEqual(find_city.status_code, 200)
        self.assertEqual(find_city.json()["name"], find_city_with_lang.json()["name"])
