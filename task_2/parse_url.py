import requests
from bs4 import BeautifulSoup


def request_to_url(url):
    req_ulr = requests.get(url)
    if req_ulr.status_code != 200:
        result = 'end'
    else:
        result = req_ulr.text
    return result


def parse_list(page):
    result = {}
    soup = BeautifulSoup(page, 'html.parser')
    target_div = soup.find(id='mw-pages')
    a_list = target_div.find_all('a')
    next_link = target_div.find('a', text='Следующая страница')
    if next_link == None:
        result['next_link'] = 'end'
    else:
        result['next_link'] = 'https://ru.wikipedia.org/' + next_link['href']
    execute_list = ['Предыдущая страница', 'Следующая страница']
    result['data'] = []
    for a in a_list:
        if a.text not in execute_list:
            result['data'].append(a.text)
    return result
