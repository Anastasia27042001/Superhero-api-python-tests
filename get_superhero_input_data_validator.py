def validate_data(gender, work, data_heroes):
    # в функции проверка корректности входных данных и структуры героя
    # проверка типа параметра gender
    if not isinstance(gender, str):
        raise TypeError('Параметр gender должен быть строкой')

    # проверка типа параметра work
    if not isinstance(work, bool):
        raise TypeError('Параметр work должен быть типа bool')

    # проверка наличия данных
    if not data_heroes:
        raise ValueError('Нет данных о героях')

    # проверка структуры каждого героя
    for hero in data_heroes:
        if not isinstance(hero, dict):
            raise TypeError('Неверный тип данных для героя')

        if 'appearance' not in hero:
            raise KeyError('Отсутствуют необходимые ключи в данных')

        appearance = hero['appearance']
        if not isinstance(appearance, dict):
            raise TypeError('Неверный тип данных для поля appearance')

        if 'gender' not in appearance or 'height' not in appearance:
            raise KeyError('Отсутствуют необходимые ключи в данных')

        if 'work' not in hero:
            raise KeyError('Отсутствуют необходимые ключи в данных')

        work_data = hero['work']
        if not isinstance(work_data, dict) or 'base' not in work_data:
            raise KeyError('Отсутствуют необходимые ключи в данных')


def filter_heroes(gender, work, data_heroes):
    # функция фильтрации героев по полу и статусу работы
    filtered_heroes = []

    for hero in data_heroes:
        # проверка пола
        if hero['appearance']['gender'] != gender:
            continue

        base_status = hero.get('work', {}).get('base')
        # проверка работы
        if work is False and base_status != '-':
            continue
        if work is True and base_status == '-':
            continue

        filtered_heroes.append(hero)

    return filtered_heroes