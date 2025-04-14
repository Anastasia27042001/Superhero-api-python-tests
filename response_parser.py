from heroic_fixture import superhero_data
import json

response = superhero_data()

result = []

for hero in response:
    hero_info = (hero['id'], hero['appearance']['height'], hero['work']['base'], hero['appearance']['gender'])
    result.append(hero_info)

print(json.dumps(result))