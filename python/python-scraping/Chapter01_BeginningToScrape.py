# step1
# from urllib.request import urlopen

# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(html.read())


# step2
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs.h1)
# print(bs.div)


# step3
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError

# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# except HTTPError as e:
#     print("The server returned an HTTP error")
# except URLError as e:
#     print("The server could not be found!")
# else:
#     print(html.read())


# step4
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
