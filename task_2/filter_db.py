import re
from database import select_from_db
from collections import defaultdict


def filtration():
    pattern = re.compile('^[А-ЯЁа-яё]*$')
    result_dict = defaultdict(int)
    data = select_from_db()
    count_filter = 0

    for d in data:
        animal = d[0]
        if pattern.match(animal):
            result_dict[animal[0]] += 1
            count_filter += 1

    with open('../result.txt', 'w', encoding='UTF-8') as file:
        file.write(f'Результаты\n')
        for k, v in result_dict.items():
            file.write(f'{k}:{v}\n')

    print(f'В результирующий список попало {count_filter} значений из {len(data)}')


if __name__ == '__main__':
    '''
    Вызов этой функции проверит элементы на соответствие регулярному выражению
    Сделает подсчет элементов каждой буквы
    Конечный результат в файле result.txt корневого каталога
    '''
    filtration()
