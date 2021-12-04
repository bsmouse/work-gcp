import requests
from bs4 import BeautifulSoup


import requests


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


# def getPage(url):
#     req = requests.get(url)
#     return BeautifulSoup(req.text, 'html.parser')

def getPage(url):
    """
    Utilty function used to get a Beautiful Soup object from a given URL
    """

    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    try:
        req = session.get(url, headers=headers)
    except requests.exceptions.RequestException:
        return None
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs


def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)


def scrapeLocalpay(url):
    bs = getPage(url)
    title = bs.find('title').text
    body = bs.find('div', {'class', 'container'}).text
    return Content(url, title, body)

# url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
# content = scrapeBrookings(url)
# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print(content.body)


url = 'https://web.ktgoodpay.com/gumi/registrationForm'
content = scrapeLocalpay(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)
