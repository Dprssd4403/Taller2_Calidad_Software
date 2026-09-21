import requests
from ..models import Pokemon

def sync_pokemons_from_api(limit=20):
    url = f"https://pokeapi.co/api/v2/pokemon/?offset=0&limit={limit}"
    response = requests.get(url, timeout=10)
    
    if response.status_code != 200:
        return 0

    data = response.json()
    created_count = 0

    for item in data.get('results', []):
        detail_res = requests.get(item['url'], timeout=10)
        if detail_res.status_code == 200:
            pdata = detail_res.json()
            poke_id = pdata['id']
            
            _, created = Pokemon.objects.get_or_create(
                poke_id=poke_id,
                defaults={
                    'name': pdata['name'],
                    'height': pdata['height'] / 10.0,
                    'weight': pdata['weight'] / 10.0,
                    'sprite_url': pdata['sprites']['front_default'] or ''
                }
            )
            if created:
                created_count += 1

    return created_count