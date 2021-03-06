def form_set(data):
    result = []
    for k in range(0, len(data), 2):
        for el in range(data[k], data[k + 1] + 1):
            result.append(el)
    return set(result)


def cross_time(data):
    set_lesson = form_set(data['lesson'])
    set_pupil = form_set(data['pupil'])
    set_tutor = form_set(data['tutor'])
    result = set_lesson.intersection(set_pupil, set_tutor)
    total_time = len(result)
    return f'Общее время присутствия ученика и учителя на уроке: {total_time} сек или {round(total_time / 60)} минут'


def get_times(input_obj):
    result = []
    for el in input_obj:
        time = cross_time(el['data'])
        answer = el['answer']
        result.append((f'Запрос {answer}', time))
    return result


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    '''
    Алгоритм выполнения:
    При запуске функции get_timex обходим элементы списка, для каждого словаря data составляем множества (form_set),
    представляющие собой секунды присутствия на уроке - отдельно для ученика,урока и учителя
    Методом intersection ищем пересечение множеств (cross_time) - длина этого множества является совместным временем присутствия
    на уроке.
    '''
    print(get_times(tests))

'''
Результаты:
[('Запрос 3117', 'Общее время присутствия ученика и учителя на уроке: 3121 сек или 52 минут'),
 ('Запрос 3577', 'Общее время присутствия ученика и учителя на уроке: 3580 сек или 60 минут'),
 ('Запрос 3565', 'Общее время присутствия ученика и учителя на уроке: 3567 сек или 59 минут')]
'''
