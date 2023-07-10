#!/usr/bin/python3
# import requests

# params = {'username': 'blueapm', 'password': 'password'}
# r = requests.post(
#     'http://pythonscraping.com/pages/cookies/welcome.php', params)
# print('Cookie is set to:')
# print(r.cookies.get_dict())
# print('Going to profile page...')
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
#                  cookies=r.cookies)
# print(r.text)


import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as elemTree
import time


auth = HTTPBasicAuth('seoamo', '1234qwer')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
r = requests.post(
    url='http://dccl.iptime.org/stat', auth=auth, headers=headers)
# print(r.text)

root = elemTree.fromstring(r.text)
# print(root.tag)

for stream in root.findall('server/application/live/stream'):
    # print(stream.tag)
    print(stream.find('./name').text, end=' ')
    print(f'#{stream.find("./nclients").text}', end=' ')

    # seconds = int(float(stream.find("./client/time").text) / 1000)
    # dseconds = int((seconds % 3600) % 60)
    # dminites = int((seconds % 3600) / 60)
    # dhours = int(seconds/3600)
    # print(f'Time:{dhours}h{dminites:02}m{dseconds:02}s')

    seconds = int(float(stream.find("./client/time").text) / 1000)
    delta = time.gmtime(seconds)
    print(
        f'Time:{delta.tm_yday-1}d{delta.tm_hour:02}h{delta.tm_min:02}m{delta.tm_sec:02}s')
