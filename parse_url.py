import requests
from bs4 import BeautifulSoup

def parse(url):
    req_ulr = requests.get(url)
    if req_ulr.status_code !=200:
        result = 'end'
    else:
        result = req_ulr.text
    return result

def get_next_url(page):
    soup = BeautifulSoup(page, 'html.parser')
    target_div = soup.find(id='mw-pages')
    next_link = target_div.find('a', text='Следующая страница')
    if next_link == None:
        return 'end'
    else:
        result = 'https://ru.wikipedia.org/' + next_link['href']
    return result

def get_list(page):
    soup = BeautifulSoup(page,'html.parser')
    target_div = soup.find(id='mw-pages')
    a_list = target_div.find_all('a')
    execute_list = ['Предыдущая страница','Следующая страница']
    result = []
    for a in a_list:
        if a.text not in execute_list:
            result.append(a.text)
    return result