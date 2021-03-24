from model import add_to_db
from parse_url import parse, get_next_url, get_list

start_url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%83%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages'
count_page = 1

def start():
    while True:
        target_url = start_url
        page = parse(target_url)
        animal_list = get_list(page)
        for animal in animal_list:
            add_to_db(animal)
        next_url = get_next_url(page)
        if next_url == 'end':
            break
        else:
            start_url = next_url
        count_page += 1


# Для запуска парсинга запускаем функцию start()
# start()


print(f'Распарсили {count_page} страниц')


