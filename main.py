import requests
from bs4 import BeautifulSoup


#
# url1 = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D0%B7%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B5+%D1%83%D0%B6%D0%B8#mw-pages'
#
# r = requests.get(url1)
# with open('state.html','w',encoding='UTF-8') as a:
#     a.write(r.text)

# print(r.status_code)
# print(r.encoding)
# if r.status_code != 200:
#     print('no connection')

with open('state.html','r',encoding='UTF-8') as file:
    state = file.read()
soup= BeautifulSoup(state,'html.parser')
div = soup.find(id='mw-pages')
test_b = div.find('a',text='Следующая страница')
print(test_b)
next_link ='https://ru.wikipedia.org/'+test_b['href']
print(next_link)
test_a = div.find_all('a')
for links in test_a:
    print(links.text)


