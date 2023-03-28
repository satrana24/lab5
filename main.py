from random import *

def first():
    s = [1, 2, 3, 4, 5]
    num = int(input('Введите число: '))
    if num in s:
        print(f'Ваше число: {num}')
        print('Исходный список:', *s)
        print('Поздравляю, Вы угадали число!')
    else:
        print(f'Ваше число: {num}')
        print('Исходный список:', *s)
        print('Нет такого числа!')


def second():
    s = [1, 1, 3, 3, 7, 1]
    # создаём словарь
    repeat = {str(i) for i in s if s.count(i) > 1}
    if len(repeat) < 1:
        print('no duplicates')
    else:
        print('duplicate:', ' '.join(repeat))


def third():
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    question = int(input('Введите количество выходных, которое хотите иметь в неделю: '))
    job = week[:-question]
    # start stop step
    weekend = week[:-question-1:-1]
    if 1 < question <= 7:
        print('Ваши выходные дни:', *weekend)
        print('Ваши рабочие дни:', *job)
    elif question == 0:
        print('Ваши выходные дни: -.')
        print('Ваши рабочие дни:', *week)


def fourth():
    students1 = ['Ягодкин', 'Коршунов', 'Державин', 'Сидоров', 'Петров', 'Васечкин', 'Ломоносов',
                              'Саввин', 'Ершов', 'Силивин']
    students2 = ['Иванов', 'Стиценко', 'Головко', 'Бодров', 'Бондаренко', 'Куницын', 'Косульников',
                               'Воротынцев', 'Купоросов', 'Герц']
    sport_team = tuple(sample(students1, 5)) + tuple(sample(students2, 5))
    print('Исходный список первой группы:', *students1)
    print('Исходный список второй группы', *students2)
    print('Список спортивной команды:', *sorted(sport_team))
    print('Количество человек в спортивной команде:', len(sport_team))
    if 'Иванов' in sport_team:
        print(f'Иванов входит в список спортивной команды, его фамилия встречается {sport_team.count("Иванов")} раз')
    else:
        print('Иванов в список спортивной команды не входит')


fourth()
