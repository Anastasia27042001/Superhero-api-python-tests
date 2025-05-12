from get_superhero_input_data_validator import validate_data, filter_heroes

def parse_height(height_str):
    # функция преобразования высоты в корректный формат
    try:
        height_value, unit = height_str.split()
        height_value = float(height_value)

        if 'cm' in unit.lower():
            return height_value  # уже в см
        elif 'm' in unit.lower():
            return height_value * 100  # перевод метров в см
        else:
            return 0  # если единицы измерения некорректны
    except ValueError:
        return 0  # если не удалось распарсить высоту


def get_tallest_superhero(gender: str, work: bool, data_heroes: list):
    # функция поиска самого высокого супер героя по заданным параметрам
    # валидация данных
    validate_data(gender, work, data_heroes)

    # фильтрация героев
    filtered_heroes = filter_heroes(gender, work, data_heroes)

    tallest_hero = None
    max_height = 0

    for hero in filtered_heroes:
        # парсинг высоты
        height_str = hero['appearance']['height'][1]
        height_parsed = parse_height(height_str)

        # обновление максимальной высоты
        if height_parsed > max_height:
            max_height = height_parsed
            tallest_hero = hero

    # добавление высоты в результат
    if tallest_hero:
        tallest_hero['height_in_cm'] = max_height

    return tallest_hero

