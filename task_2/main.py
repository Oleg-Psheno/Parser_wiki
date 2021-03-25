from task_2.database import add_to_db
from task_2.parse_url import request_to_url, parse_list

start_url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%83%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages'


def start():
    count_page = 1
    count_animals = 0
    next_url = start_url
    while True:
        page = request_to_url(next_url)
        parse_data = parse_list(page)
        animal_list = parse_data['data']
        count_animals += len(animal_list)
        for animal in animal_list:
            add_to_db(animal)
        next_url = parse_data['next_link']
        if next_url == 'end':
            break
        print(f'Парсим старницу № {count_page} добавлено в БД {len(animal_list)} элементов')
        count_page += 1

    print(f'Было просмотрено {count_page} страниц, добавлено в БД {count_animals} видов животных')


if __name__ == '__main__':
    confirm = input('Чтобы запустить программу введите цифру 1: ')
    if confirm == '1':
        start()
