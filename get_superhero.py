import requests

def get_tallest_superhero(gender: str, work: bool, data_heroes: list):
    if not data_heroes:
        raise ValueError('Нет данных о героях')

    # проверка типа параметра work
    if not isinstance(work, bool):
        return None

    tallest_hero = None
    max_height = 0

    for hero in data_heroes:
        try:
            # проверяем наличие необходимых ключей
            if 'appearance' not in hero or 'gender' not in hero['appearance'] or 'height' not in hero['appearance']:
                raise KeyError('Отсутствуют необходимые ключи в данных')
            if 'work' not in hero or 'base' not in hero['work']:
                raise KeyError('Отсутствуют необходимые ключи в данных')

            # проверяем соответствие параметров
            if hero['appearance']['gender'] != gender:
                continue
            if work == False:
                if hero['work']['base'] != "-":
                    continue
            else:
                if hero['work']['base'] == "-":
                    continue

            height_str = hero['appearance']['height'][1]

            try:  # перевод высоты в см
                height_value, unit = height_str.split()
                height_value = float(height_value)

                if "cm" in unit.lower():
                    height_parsed = height_value  # уже в см
                elif "m" in unit.lower():
                    height_parsed = height_value * 100  # перевод метров в см
                else:
                    height_parsed = 0  # если единицы измерения некорректны

            except ValueError:
                height_parsed = 0  # если не удалось распарсить высоту

            if height_parsed > max_height:
                max_height = height_parsed
                tallest_hero = hero

            if tallest_hero:
                tallest_hero['height_in_cm'] = max_height

        except KeyError as e:
            # перехватываем исключение и повторно вызываем его с нужным сообщением
            raise KeyError('Отсутствуют необходимые ключи в данных') from e

    return tallest_hero

