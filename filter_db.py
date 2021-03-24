import re
from model import select_from_db
from collections import defaultdict

# создаем регулярное выражение для отсеивания элементов на английском языке, а также
# элементов, состоящих из нескольких слов

pattern = re.compile('^[А-ЯЁа-яё]*$')


result_dict = defaultdict(int)

data = select_from_db()

for d in data:
    animal = d[0]
    if pattern.match(animal):
        result_dict[animal[0]] += 1

with open('result.txt','w',encoding='UTF-8') as file:
    file.write(f'Результаты\n')
    for k,v in result_dict.items():
        file.write(f'{k}:{v}\n')

