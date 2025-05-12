import pytest
import requests

@pytest.fixture(scope='module')
def superhero_data():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    assert response.status_code == 200, 'responce.status_code'
    data_heroes = response.json()

    return data_heroes

# хранилище с валидными значениями
@pytest.fixture(scope='module')
def equivalence_values():

    return [
        ('Male', True, 728),
        ('Male', False, 681),
        ('Female', True, 284),
        ('Female', False, 120),
    ]

# хранилище для пограничного тестирования с превышающим значением (+1 см)
def get_boundary_values_higher():
    return {
        ("Male", True): {"id": 9989, "name": "Bill", "appearance": {"gender": "Male", "height": ["7'2", "30481 cm"]},
         "work": {"occupation": "-", "base": "Gravity Falls"}},
        ("Male", False): {"id": 9999, "name": "Pikachu", "appearance": {"gender": "Male", "height": ["7'2", "1521 cm"]},
         "work": {"occupation": "-", "base": "-"}},
        ("Female", True): {"id": 9979, "name": "Bri", "appearance": {"gender": "Female", "height": ["7'2", "6251 cm"]},
         "work": {"occupation": "-", "base": "Wisteria Lane"}},
        ("Female", False): {"id": 9959, "name": "Linette", "appearance": {"gender": "Female", "height": ["7'2", "219 cm"]},
         "work": {"occupation": "-", "base": "-"}}
    }


@pytest.fixture(scope='module')
def boundary_values_higher(superhero_data):
    boundary_heroes = list(get_boundary_values_higher().values())

    return superhero_data + boundary_heroes


# хранилище для пограничного тестирования с меньшим значением (-1 см)
@pytest.fixture(scope='module')
def boundary_values_lower(superhero_data):
    boundary_heroes = [
        {"id": 9949, "name": "Walter", "appearance": {"gender": "Male", "height": ["7'2", "30479 cm"]},
         "work": {"occupation": "-", "base": "Albuquerque"}},
        {"id": 9939, "name": "Silvio", "appearance": {"gender": "Male", "height": ["7'2", "1519 cm"]},
         "work": {"occupation": "-", "base": "-"}},
        {"id": 9929, "name": "Anthony", "appearance": {"gender": "Female", "height": ["7'2", "6249 cm"]},
         "work": {"occupation": "-", "base": "North Caldwell"}},
        {"id": 9919, "name": "Darth Vader", "appearance": {"gender": "Female", "height": ["7'2", "217 cm"]},
         "work": {"occupation": "-", "base": "-"}}
        ]
    return superhero_data + boundary_heroes