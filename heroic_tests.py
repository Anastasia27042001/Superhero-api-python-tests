import pytest

import heroic_fixture
from get_superhero import get_tallest_superhero
from heroic_fixture import *

def test_equivalence_partitioning(equivalence_values, superhero_data):
    # проверка функции с валидными данными
    errors = []

    for gender, work, expected_id in equivalence_values:
        result = get_tallest_superhero(gender, work, superhero_data)

        assert result is not None, 'Не найден подходящий герой'
        actual_id = result['id']
        if actual_id != expected_id:
            errors.append(f'\nОжидался герой с id: {expected_id}, но получен id: {actual_id}')
        else:
            print(f'\nСамый высокий супергерой: {result['name']}, id: {result['id']} ({result['height_in_cm']} см)')
        if errors:
            pytest.fail('\n'.join(errors))


def test_boundary_values_higher(equivalence_values, boundary_values_higher):
    # проверка функции с данными превышающие значение (выше)
    errors = []

    expected_heroes = heroic_fixture.get_boundary_values_higher
    for gender, work, _ in equivalence_values:
        result = get_tallest_superhero(gender, work, boundary_values_higher)

        assert result is not None, 'Не найден подходящий герой'
        actual_id = result['id']
        expected_id = expected_heroes[(gender, work)]['id']

        if actual_id != expected_id:
            errors.append(f'\nОжидался герой с id: {expected_id}, но получен id: {actual_id}')
        else:
            print(f'\nСамый высокий супергерой: {result['name']}, id: {result['id']} ({result['height_in_cm']} см)')
    if errors:
        print('\n'.join(errors))
        pytest.fail()


def test_boundary_values_lower(equivalence_values, boundary_values_lower):
    # проверка функции с данными меньшего значения
    errors = []

    for gender, work, expected_id in equivalence_values:
        result = get_tallest_superhero(gender, work, boundary_values_lower)

        assert result is not None, 'Не найден подходящий герой'
        actual_id = result['id']
        if actual_id != expected_id:
            errors.append(f'\nОжидался герой с id: {expected_id}, но получен id: {actual_id}')
        else:
            print(f'\nСамый высокий супергерой: {result['name']}, id: {result['id']} ({result['height_in_cm']} см)')
    if errors:
        pytest.fail('\n'.join(errors))


def test_negative():
    # пустой список героев
    try:
        get_tallest_superhero('Male', True, [])
        assert False, 'Ожидалось исключение ValueError, но оно не было вызвано'
    except ValueError as e:
        assert str(e) == 'Нет данных о героях'

    # данные без необходимых ключей
    incomplete_data = [
        {'id': 1, 'name': 'Hero1'},  # отсутствует 'appearance'
        {'id': 2, 'name': 'Hero2', 'appearance': {'gender': 'Male'}},  # отсутствует 'height'
    ]
    try:
        get_tallest_superhero('Male', True, incomplete_data)
        assert False, 'Ожидалось исключение KeyError, но оно не было вызвано'
    except KeyError as e:
        assert str(e) == "'Отсутствуют необходимые ключи в данных'"

    # неверное значение gender
    invalid_gender_data = [{'id': 1, 'name': 'Hero1', 'appearance': {'gender': 'Unknown', 'height': ['6''0', '183 cm']}, 'work': {'base': '-' }},]
    result = get_tallest_superhero('Unknown', True, invalid_gender_data)
    assert result is None, 'Функция должна вернуть None для неверного gender'

    # неверное значение work
    invalid_work_data = [
        {'id': 1, 'name': 'Hero1', 'appearance': {'gender': 'Male', 'height': ['6''0', '183 cm']}, 'work': {'base': 'Invalid'}},
    ]
    try:
        get_tallest_superhero('Male', 'NotBoolean', invalid_work_data)
        assert False, 'Ожидалось исключение TypeError, но оно не было вызвано'
    except TypeError as e:
        assert str(e) == 'Параметр work должен быть типа bool'
    assert result is None, 'Функция должна вернуть None для неверного work'

    # некорректный формат роста
    invalid_height_data = [
        {'id': 1, 'name': 'Hero1', 'appearance': {'gender': 'Male', 'height': ['Invalid', 'NaN']}, 'work': {'base': '-' }},
    ]
    result = get_tallest_superhero('Male', True, invalid_height_data)
    assert result is None, 'Функция должна вернуть None для некорректного роста'

    # отсутствие подходящих героев
    no_matching_heroes_data = [
        {'id': 1, 'name': 'Hero1', 'appearance': {'gender': 'Female', 'height': ["6'0", '183 cm']}, 'work': {'base': '-' }},
    ]
    result = get_tallest_superhero('Male', True, no_matching_heroes_data)
    assert result is None, 'Функция должна вернуть None, если нет подходящих героев'

    # одинаковый рост
    same_height_heroes = [
        {'id': 1, 'name': 'Hero1', 'appearance': {'gender': 'Male', 'height': ["6'0", '183 cm']},
         'work': {'base': '-'}},
        {'id': 2, 'name': 'Hero2', 'appearance': {'gender': 'Male', 'height': ["6'0", '183 cm']},
         'work': {'base': '-'}},
        {'id': 3, 'name': 'Hero3', 'appearance': {'gender': 'Male', 'height': ["6'0", '183 cm']},
         'work': {'base': '-'}},
        {'id': 4, 'name': 'Hero4', 'appearance': {'gender': 'Male', 'height': ["6'0", '183 cm']},
         'work': {'base': '-'}},
        {'id': 5, 'name': 'Hero5', 'appearance': {'gender': 'Male', 'height': ["6'0", '183 cm']},
         'work': {'base': '-'}}
    ]
    result = get_tallest_superhero('Male', False, same_height_heroes)
    assert result is not None, 'Функция вернула не пустой результат'
    print(f'\n{result}')
    assert result['id'] == 1, 'Функция должна вернуть 1 id'
