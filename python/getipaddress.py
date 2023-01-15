#!/usr/bin/python3
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    # location_data = {
    #     "ip": ip_address,
    #     "city": response.get("city"),
    #     "region": response.get("region"),
    #     "country": response.get("country_name")
    # }
    # return location_data
    return response


def print_location(location_data):
    for key, val in location_data.items():
        print(key, '-', val)


print_location(get_location())
